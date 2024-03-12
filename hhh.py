import pygame as pg
# from collections import deque
# from random import choice

WIDTH = 1200
HEIGHT = 750
SIZE = [WIDTH, HEIGHT]
a = 50
columns = WIDTH // a
rows = HEIGHT // a
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
    x_paint = 600
    y_paint = 100
    first_row = 1
    for i in range(7):
        x_f = x_paint
        y_f = y_paint
        for j in range(first_row):
            h = Hexagon(x_paint, y_paint)
            h.paint()
            x_paint += 2 * half
        x_paint = x_f - half
        y_paint = y_f + 1.5 * a
        first_row += 1

    pg.display.flip()
    time.tick(100)