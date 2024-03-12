import pygame as pg
from collections import deque
from random import choice

WIDTH = 1200
HEIGHT = 750
SIZE = [WIDTH, HEIGHT]
a = 10

HEX_CONST = (3 / 4) ** 0.5
# half = HEX_CONST * a
half = 20
hei = 0.5 * a

flag = 1



class Hexagon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True, True, True]
        self.visited = False

    def paint(self):
        pg.draw.line(screen, 'black', (self.x, self.y), (self.x + half, self.y - hei))
        x1 = self.x + half
        y1 = self.y - hei
        pg.draw.line(screen, 'black', (x1, y1), (x1 + half, y1 + hei))
        x1 = x1 + half
        y1 = y1 + hei
        pg.draw.line(screen, 'black', (x1, y1), (x1, y1 + a))
        y1 += a
        pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 + hei))
        x1 = x1 - half
        y1 = y1 + hei
        pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 - hei))
        x1 = x1 - half
        y1 = y1 - hei
        pg.draw.line(screen, 'black', (x1, y1), (x1, y1 - a))

pg.init()

screen = pg.display.set_mode(SIZE)
time = pg.time.Clock()
x = 0
y = 0
while True:
    screen.fill('white')

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())

    x_paint = 600 - half
    rows = (1500 - a) // (3 * a)
    ost = (1500 - a) % (3 * a)
    y_paint = ost / 2
    rise = True
    first_row = 1
    for i in range(rows):
        print(first_row)
        x_f = x_paint
        y_f = y_paint
        for j in range(first_row):
            h = Hexagon(x_paint, y_paint)
            h.paint()
            x_paint += 2 * half

        if first_row > rows // 2 + 1:
            rise = False
        if rise:
            first_row += 1
            x_paint = x_f - half
            y_paint = y_f + 1.5 * a
        else:
            first_row -= 1
            x_paint = x_f + half
            y_paint = y_f + 1.5 * a

    pg.display.flip()
    time.tick(100)