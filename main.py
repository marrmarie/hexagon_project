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
    center_start = 27
    center_finish = 35
    grid = [-1 for i in range(61)]
elif flag == 2:
    a = 42.3
    count_row = 6
    rows = 8
    center_start = 52
    center_finish = 63
    grid = [-1 for i in range(114)]
elif flag == 3:
    a = 32.6
    count_row = 7
    rows = 12
    center_start = 85
    center_finish = 99
    grid = [-1 for i in range(183)]
elif flag == 4:
    a = 26.4
    count_row = 9
    rows = 16
    center_start = 136
    center_finish = 154
    grid = [-1 for i in range(289)]
elif flag == 5:
    a = 19.2
    count_row = 11
    rows = 24
    center_start = 246
    center_finish = 270
    grid = [-1 for i in range(515)]

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

    def paint(self):
        if self.walls[3]:
            pg.draw.line(screen, 'black', (self.x, self.y), (self.x + half, self.y - hei))
        x1 = self.x + half
        y1 = self.y - hei
        if self.walls[2]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 + half, y1 + hei))
        x1 = x1 + half
        y1 = y1 + hei
        if self.walls[1]:
            pg.draw.line(screen, 'black', (x1, y1), (x1, y1 + a))
        y1 += a
        if self.walls[5]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 + hei))
        x1 = x1 - half
        y1 = y1 + hei
        if self.walls[4]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 - hei))
        x1 = x1 - half
        y1 = y1 - hei
        if self.walls[0]:
            pg.draw.line(screen, 'black', (x1, y1), (x1, y1 - a))
        # base_font2 = pg.font.Font(None, 20)
        # f1 = base_font2.render(str(self.number), 1, 'black')
        # screen.blit(f1, (self.x + half, self.y + 0.5 * a))

    def choice_to_go_first_half(self, grid):
        neighbours = []
        n1 = grid[self.number - 1 - 1]
        n2 = grid[self.number + 1 - 1]
        n3 = grid[self.number - self.prev_line - 1]
        n4 = grid[self.number - self.prev_line - 1 - 1]
        n5 = grid[self.number + self.prev_line + 1 - 1]
        n6 = grid[self.number + self.prev_line + 2 - 1]

        if n1.number <= len(grid) and n1.number > 0 and not n1.visited:
            if not n1.visited and n1.x == self.x - 2 * half:
                neighbours.append(n1)

        if n2.number <= len(grid) and n2.number > 0 and not n2.visited:
            if not n2.visited and n2.x == self.x + 2 * half:
                neighbours.append(n2)

        if n3.number <= len(grid) and n3.number > 0 and not n3.visited:
            if not n3.visited and n3.x == self.x + half and n3.y == self.y - 1.5 * a:
                neighbours.append(n3)

        if n4.number <= len(grid) and n4.number > 0 and not n4.visited:
            if not n4.visited and n4.x == self.x - half and n4.y == self.y - 1.5 * a:
                neighbours.append(n4)

        if n5.number <= len(grid) and n5.number > 0 and not n5.visited:
            if not n5.visited and n5.x == self.x - half and n5.y == self.y + 1.5 * a:
                neighbours.append(n5)

        if n6.number <= len(grid) and n6.number > 0 and not n6.visited:
            if not n6.visited and n6.x == self.x + half and n6.y == self.y + 1.5 * a:
                neighbours.append(n6)

        if len(neighbours) != 0:
            return choice(neighbours)
        return False

    def choice_to_go_second_half(self, grid):
        neighbours = []
        n1 = grid[self.number - 1 - 1]
        if n1.number <= len(grid) and n1.number > 0 and not n1.visited:
            if not n1.visited and n1.x == self.x - 2 * half:
                neighbours.append(n1)

        if self.number + 1 - 1 < len(grid):
            n2 = grid[self.number + 1 - 1]
            if n2.number <= len(grid) and n2.number > 0 and not n2.visited:
                if not n2.visited and n2.x == self.x + 2 * half:
                    neighbours.append(n2)
        if self.number - self.prev_line + 1 - 1 < len(grid):
            n3 = grid[self.number - self.prev_line + 1 - 1]
            if n3.number <= len(grid) and n3.number > 0 and not n3.visited:
                if not n3.visited and n3.x == self.x + half and n3.y == self.y - 1.5 * a:
                    neighbours.append(n3)
        n4 = grid[self.number - self.prev_line - 1]
        if n4.number <= len(grid) and n4.number > 0 and not n4.visited:
            if not n4.visited and n4.x == self.x - half and n4.y == self.y - 1.5 * a:
                neighbours.append(n4)
        if self.number + self.prev_line - 2 - 1 < len(grid):
            n5 = grid[self.number + self.prev_line - 2 - 1]
            if n5.number <= len(grid) and n5.number > 0 and not n5.visited:
                if not n5.visited and n5.x == self.x - half and n5.y == self.y + 1.5 * a:
                    neighbours.append(n5)
        if self.number + self.prev_line - 1 - 1 < len(grid):
            n6 = grid[self.number + self.prev_line - 1 - 1]
            if n6.number <= len(grid) and n6.number > 0 and not n6.visited:
                if not n6.visited and n6.x == self.x + half and n6.y == self.y + 1.5 * a:
                    neighbours.append(n6)

        if len(neighbours) != 0:
            return choice(neighbours)
        return False

    def choice_to_go_center(self, grid):
        neighbours = []

        n1 = grid[self.number - 1 - 1]
        n2 = grid[self.number + 1 - 1]
        n3 = grid[self.number - self.prev_line - 1]
        n4 = grid[self.number - self.prev_line - 1 - 1]
        n5 = grid[self.number + self.prev_line - 1]
        n6 = grid[self.number + self.prev_line + 1 - 1]

        if n1.number <= len(grid) and n1.number > 0 and not n1.visited:
            if not n1.visited and n1.x == self.x - 2 * half:
                neighbours.append(n1)

        if n2.number <= len(grid) and n2.number > 0 and not n2.visited:
            if not n2.visited and n2.x == self.x + 2 * half:
                neighbours.append(n2)

        if n3.number <= len(grid) and n3.number > 0 and not n3.visited:
            if not n3.visited and n3.x == self.x + half and n3.y == self.y - 1.5 * a:
                neighbours.append(n3)

        if n4.number <= len(grid) and n4.number > 0 and not n4.visited:
            if not n4.visited and n4.x == self.x - half and n4.y == self.y - 1.5 * a:
                neighbours.append(n4)

        if n5.number <= len(grid) and n5.number > 0 and not n5.visited:
            if not n5.visited and n5.x == self.x - half and n5.y == self.y + 1.5 * a:
                neighbours.append(n5)

        if n6.number <= len(grid) and n6.number > 0 and not n6.visited:
            if not n6.visited and n6.x == self.x + half and n6.y == self.y + 1.5 * a:
                neighbours.append(n6)

        if len(neighbours) != 0:
            return choice(neighbours)
        return False


def red_dots(grid):
    for i in range(len(grid)):
        h = grid[i]
        if h.visited:
            pg.draw.circle(screen, 'red', (h.x + half, h.y + 0.5 * a), 10)


def true_false_cells_first_half(now, next):
    if next.number == now.number - 1:
        now.walls[0] = False
        next.walls[1] = False
    elif next.number == now.number + 1:
        now.walls[1] = False
        next.walls[0] = False
    elif next.number == now.number - now.prev_line:
        now.walls[2] = False
        next.walls[4] = False
    elif next.number == now.number - now.prev_line - 1:
        now.walls[3] = False
        next.walls[5] = False
    elif next.number == now.number + now.prev_line + 1:
        now.walls[4] = False
        next.walls[2] = False
    elif next.number == now.number + now.prev_line + 2:
        now.walls[5] = False
        next.walls[3] = False


def true_false_cells_second_half(now, next):
    if next.number == now.number - 1:
        now.walls[0] = False
        next.walls[1] = False
    elif next.number == now.number + 1:
        now.walls[1] = False
        next.walls[0] = False
    elif next.number == now.number - now.prev_line + 1:
        now.walls[2] = False
        next.walls[4] = False
    elif next.number == now.number - now.prev_line:
        now.walls[3] = False
        next.walls[5] = False
    elif next.number == now.number + now.prev_line - 2:
        now.walls[4] = False
        next.walls[2] = False
    elif next.number == now.number + now.prev_line - 1:
        now.walls[5] = False
        next.walls[3] = False


def true_false_cells_center(now, next):
    if next.number == now.number - 1:
        now.walls[0] = False
        next.walls[1] = False
    elif next.number == now.number + 1:
        now.walls[1] = False
        next.walls[0] = False
    elif next.number == now.number - now.prev_line:
        now.walls[2] = False
        next.walls[4] = False
    elif next.number == now.number - now.prev_line - 1:
        now.walls[3] = False
        next.walls[5] = False
    elif next.number == now.number + now.prev_line:
        now.walls[4] = False
        next.walls[2] = False
    elif next.number == now.number + now.prev_line + 1:
        now.walls[5] = False
        next.walls[3] = False


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
        if not rise:
            grid[i] = Hexagon(x_paint, y_paint, i + 1, row_in_grid, j + 1, count_row + 1)
        else:
            grid[i] = Hexagon(x_paint, y_paint, i + 1, row_in_grid, j + 1, count_row - 1)
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

cell_now = grid[0]
cell_now.visited = True
queue = deque()
grid[0].visited = True

x = grid[0].x
y = grid[0].y
while True:
    screen.fill('white')

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_e:
                x += half
                y -= 1.5 * a
            if i.key == pg.K_d:
                x += half * 2
            if i.key == pg.K_x:
                x += half
                y += 1.5 * a
            if i.key == pg.K_z:
                x -= half
                y += 1.5 * a
            if i.key == pg.K_a:
                x -= half * 2
            if i.key == pg.K_w:
                x -= half
                y -= 1.5 * a

    if cell_now.number < center_start:
        next_c = cell_now.choice_to_go_first_half(grid)
    elif cell_now.number > center_finish:
        next_c = cell_now.choice_to_go_second_half(grid)
    else:
        next_c = cell_now.choice_to_go_center(grid)

    if next_c:
        next_c.visited = True
        queue.append(cell_now)
        if cell_now.number < center_start:
            true_false_cells_first_half(cell_now, next_c)
        elif cell_now.number > center_finish:
            true_false_cells_second_half(cell_now, next_c)
        else:
            true_false_cells_center(cell_now, next_c)

        cell_now = next_c
    elif queue:
        cell_now = queue.pop()
    paint_hexagons(x_paint, y_paint, half, count_row)
    pg.draw.rect(screen, 'black', (cell_now.x, cell_now.y, 2 * half, a))
    red_dots(grid)
    pg.draw.rect(screen, 'green', (x, y, 2 * half, a), 10)
    pg.display.flip()
    time.tick(100)
