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
    grid = [-1 for i in range(61)]
elif flag == 2:
    a = 42.3
    count_row = 6
    rows = 8
    grid = [-1 for i in range(114)]
elif flag == 3:
    a = 32.6
    count_row = 7
    rows = 12
    grid = [-1 for i in range(183)]
elif flag == 4:
    a = 26.4
    count_row = 9
    rows = 16
    grid = [-1 for i in range(289)]
elif flag == 5:
    a = 19.2
    count_row = 11
    rows = 24
    grid = [-1 for i in range(515)]
start = 0

HEX_CONST = (3 / 4) ** 0.5
half = HEX_CONST * a
hei = 0.5 * a
x_paint = 600 - count_row * half
y_paint = 0.5 * a



HEX_CONST = (3 / 4) ** 0.5
half = HEX_CONST * a
hei = 0.5 * a



class Hexagon:
    def __init__(self, x, y, n, row, col, prev_line):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True, True, True]
        self.visited = False
        self.number = n
        self.row = row
        self.col = col
        self.prev_line = prev_line


    # def dfs(self, start, grid):
    #     self.visited = True


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


    def choice_to_go(self, grid):
        neighbours = []
        n1 = self.number - 1
        n2 = self.number + 1
        n3 = self.number - self.prev_line
        n4 = n3 - 1
        n5 = self.number + self.prev_line + 1
        n6 = self.number + self.prev_line + 2
        if n1 <= len(grid):
            if not grid[n1 - 1].visited and grid[n1 - 1].x == self.x - 2 * half:
                neighbours.append(n1)
        if n2 <= len(grid):
            if not grid[n2 - 1].visited and grid[n2 - 1].x == self.x + 2 * half:
                neighbours.append(n2)
        if n3 <= len(grid):
            if not grid[n3 - 1].visited and grid[n3 - 1].x == self.x + half and grid[n3 - 1].y == self.y - 1.5 * a:
                neighbours.append(n3)
        if n4 <= len(grid):
            if not grid[n4 - 1].visited and grid[n4 - 1].x == self.x - half and grid[n4 - 1].y == self.y - 1.5 * a:
                neighbours.append(n4)
        if n5 <= len(grid):
            if not grid[n5 - 1].visited and grid[n5 - 1].x == self.x - half and grid[n5 - 1].y == self.y + 1.5 * a:
                neighbours.append(n5)
        if n6 <= len(grid):
            if not grid[n6 - 1].visited and grid[n6 - 1].x == self.x + half and grid[n6 - 1].y == self.y + 1.5 * a:
                neighbours.append(n6)

        if len(neighbours) != 0:
            return choice(neighbours)
        return False



def paint_hexagons(x_paint, y_paint, half, count_row):
    for i in range(len(grid)):
        grid[i].paint()


rise = True
first_row = count_row
i = 0
row_in_grid = 0
while count_row != first_row - 1:
    x_f = x_paint
    y_f = y_paint
    row_in_grid += 1
    for j in range(count_row):
        grid[i] = Hexagon(x_paint, y_paint, i, row_in_grid, j + 1, count_row - 1)
        x_paint += 2 * half
        i += 1

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



while True:
    screen.fill('white')

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # if i.type == pg.MOUSEBUTTONDOWN:
        #     print(pg.mouse.get_pos())

    paint_hexagons(x_paint, y_paint, half, count_row)
    pg.display.flip()
    time.tick(100)




