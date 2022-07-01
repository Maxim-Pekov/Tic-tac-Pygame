import pygame
pygame.init()
win = pygame.display.set_mode((600,400))                          # Задание размеров окна
img = pygame.image.load('key.png')                          # загрузка иконки
pygame.display.set_caption('Крестики-Нолики', 'Крестик')    # Изменение заголовка окна
pygame.display.set_icon(img)                                # установка иконки в верхний левый угол

font = pygame.font.SysFont('comicsansms', 30)               # Задание шрифта в переменную
text = font.render('Какой-то текст', 1, 'white')            # отображение шрифта в окне приложения

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       # Обработка события нажатия на крестик закрытия окна
            quit()
        win.blit(text, (0, 0))                              # Прикрипление текста к верхнему левому углу
        pygame.display.update()
