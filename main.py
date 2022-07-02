import pygame
import sys

def check_win(mas, sign):
    zeroz = 0
    for i in mas:
        zeroz += i.count(0)
        if i.count(sign) == 3:
            return sign
    for j in range(3):
        if mas[0][j] == sign and mas[1][j] == sign and mas[2][j] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroz == 0:
        return 'PIES'
    return False
pygame.init()

img = pygame.image.load('key.png')  # загрузка иконки
pygame.display.set_caption('Крестики-Нолики', 'Крестик')  # Изменение заголовка окна
pygame.display.set_icon(img)  # установка иконки в верхний левый угол

font = pygame.font.SysFont('comicsansms', 100)  # Задание шрифта в переменную
text = font.render('Какой-то текст', 1, 'white')  # отображение шрифта в окне приложения
clock = pygame.time.Clock()
FPS = 60
width = height = 80
margin = 20
win = pygame.display.set_mode(
    (width * 3 + margin * 4, height * 3 + margin * 4))  # Задание размеров окна, зависит от размера кнопок
mas = [[0] * 10 for i in range(10)]
queue = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Обработка события нажатия на крестик закрытия окна
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(x_mouse, y_mouse)
            column = x_mouse // (margin + width)
            row = y_mouse // (margin + height)
            if mas[row][column] == 0:
                if queue % 2 == 0:
                    mas[row][column] = 'X'
                else:
                    mas[row][column] = 'O'
                queue += 1
        elif event.type == pygame.KEYDOWN and pygame.K_SPACE:
            mas = [[0] * 10 for i in range(10)]
            queue = 0


    clock.tick(FPS)
    win.fill('black')
    for row in range(3):
        for col in range(3):
            if mas[row][col] == 'X':
                color = 'red'
                # pygame.draw.line(win, 'white', (c, w), (c + width, w + height), 5)
            elif mas[row][col] == 'O':
                color = 'green'
            else:
                color = 'white'
            c = col * width + (col + 1) * margin
            w = row * height + (row + 1) * margin
            pygame.draw.rect(win, color,
                             (c, w, width, height))  # Рисуем красный квадрат в окне win, левый верхний угол в 0, 0
            if color == 'red':
                pygame.draw.line(win, 'white', (c + 5, w + 5), (c + width - 5, w + height - 5), 5)
                pygame.draw.line(win, 'white', (c + 5, w + height - 5), (c - 5 + width, w + 5),  5)
            elif color == 'green':
                pygame.draw.circle(win, 'white', (c + width//2, w + width//2), width//2-5,  5)
    if (queue-1) %2 == 0:
        game_over = check_win(mas, 'X')
    else:
        game_over = check_win(mas, 'O')
    if game_over:
        win.fill('black')
        t = font.render(game_over, 1, 'white')
        win.blit(t, ((width*2+margin*4)//2, (width*2+margin*4)//2))

    pygame.display.update()
