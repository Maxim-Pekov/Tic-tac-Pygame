import pygame

pygame.init()

img = pygame.image.load('key.png')  # загрузка иконки
pygame.display.set_caption('Крестики-Нолики', 'Крестик')  # Изменение заголовка окна
pygame.display.set_icon(img)  # установка иконки в верхний левый угол

font = pygame.font.SysFont('comicsansms', 30)  # Задание шрифта в переменную
text = font.render('Какой-то текст', 1, 'white')  # отображение шрифта в окне приложения
clock = pygame.time.Clock()
FPS = 60
width = height = 40
margin = 20
win = pygame.display.set_mode(
    (width * 10 + margin * 11, height * 10 + margin * 11))  # Задание размеров окна, зависит от размера кнопок
mas = [[0] * 10 for i in range(10)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Обработка события нажатия на крестик закрытия окна
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(x_mouse, y_mouse)
            column = x_mouse // (margin + width)
            row = y_mouse // (margin + height)
            mas[row][column] ^= 1

    clock.tick(FPS)
    win.fill('black')
    for row in range(10):
        for col in range(10):
            if mas[row][col] == 0:
                color = 'red'
            else:
                color = 'white'
            c = col * width + (col + 1) * margin
            w = row * height + (row + 1) * margin
            pygame.draw.rect(win, color,
                             (c, w, width, height))  # Рисуем красный квадрат в окне win, левый верхний угол в 0, 0
    pygame.display.update()
