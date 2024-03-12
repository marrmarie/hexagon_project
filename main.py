import pygame as pg
from collections import deque
from random import choice

WIDTH = 1200
HEIGHT = 850
SIZE = [WIDTH, HEIGHT]
screen = pg.display.set_mode(SIZE)
time = pg.time.Clock()
flag = 1
pg.init()


if flag == 1:
    a = 60
    count_row = 5
    rows = 4
elif flag == 2:
    a = 42.3
    count_row = 6
    rows = 8
elif flag == 3:
    a = 32.6
    count_row = 7
    rows = 12
elif flag == 4:
    a = 26.4
    count_row = 9
    rows = 16
elif flag == 5:
    a = 19.2
    count_row = 11
    rows = 24

HEX_CONST = (3 / 4) ** 0.5
half = HEX_CONST * a
hei = 0.5 * a
x_paint = 600 - count_row * half
y_paint = 0.5 * a



HEX_CONST = (3 / 4) ** 0.5
half = HEX_CONST * a
hei = 0.5 * a



class Hexagon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True, True, True]
        self.visited = False

    def paint(self):
        if self.walls[0]:
            pg.draw.line(screen, 'black', (self.x, self.y), (self.x + half, self.y - hei))
        x1 = self.x + half
        y1 = self.y - hei
        if self.walls[1]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 + half, y1 + hei))
        x1 = x1 + half
        y1 = y1 + hei
        if self.walls[2]:
            pg.draw.line(screen, 'black', (x1, y1), (x1, y1 + a))
        y1 += a
        if self.walls[3]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 + hei))
        x1 = x1 - half
        y1 = y1 + hei
        if self.walls[4]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 - hei))
        x1 = x1 - half
        y1 = y1 - hei
        if self.walls[5]:
            pg.draw.line(screen, 'black', (x1, y1), (x1, y1 - a))


def paint_hexagons(x_paint, y_paint, half, count_row):
    rise = True
    first_row = count_row
    while count_row != first_row - 1:
        x_f = x_paint
        y_f = y_paint
        for j in range(count_row):
            h = Hexagon(x_paint, y_paint)
            h.paint()
            x_paint += 2 * half

        if count_row > (2 * first_row + rows) // 2 + 1:
            rise = False
        if rise:
            count_row += 1
            x_paint = x_f - half
            y_paint = y_f + 1.5 * a
        else:
            count_row -= 1
            x_paint = x_f + half
            y_paint = y_f + 1.5 * a






# grid = [-1 for i in range(((rows + 2) // 2) * ((rows + 2) // 2 + 1) + (rows + 2) // 2 + 1)]
# print(len(grid))
while True:
    screen.fill('white')

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())


    paint_hexagons(x_paint, y_paint, half, count_row)
    pg.display.flip()
    time.tick(100)




