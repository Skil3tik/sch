import pygame
import random


pygame.init()


win_width = 800
win_height = 600
field_size = 50
cell_size = win_width // field_size


win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Игра Жизнь")


field = [[random.choice([0, 1]) for _ in range(field_size)] for _ in range(field_size)]


def check_rules(cell, live_neighbors):
    if cell == 1 and (live_neighbors < 2 or live_neighbors > 3):
        return 0
    elif cell == 0 and live_neighbors == 3:
        return 1
    else:
        return cell


def update_field(field):
    new_field = [[0 for _ in range(field_size)] for _ in range(field_size)]
    for i in range(field_size):
        for j in range(field_size):
            live_neighbors = sum([field[i+x][j+y] for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)])
            new_field[i][j] = check_rules(field[i][j], live_neighbors)
    return new_field


def draw_field(field):
    win.fill((0, 0, 0))
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == 1:
                pygame.draw.rect(win, (255, 255, 255), (j * cell_size, i * cell_size, cell_size, cell_size))
    pygame.display.update()


run = True
while run:
    pygame.time.delay(100) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    field = update_field(field)
    draw_field(field)

pygame.quit()
