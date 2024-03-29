import pygame as pg
from collections import deque
from random import choice

WIDTH = 1200
HEIGHT = 850
SIZE = [WIDTH, HEIGHT]
screen = pg.display.set_mode(SIZE)
time = pg.time.Clock()
flag = 1
GREEN = (52, 164, 126)
pg.init()


class Hexagon:  # класс, выполняющий операции с шестиугольниками
    def __init__(self, x, y, n, row, col, prev_line):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True, True, True]
        self.visited = False
        self.number = n
        self.row = row
        self.col = col
        self.prev_line = prev_line

    def paint(self):  # рисует один шестиугольник
        if self.walls[3]:
            pg.draw.line(screen, 'black', (self.x, self.y), (self.x + half, self.y - hei), 3)
        x1 = self.x + half
        y1 = self.y - hei
        if self.walls[2]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 + half, y1 + hei), 3)
        x1 = x1 + half
        y1 = y1 + hei
        if self.walls[1]:
            pg.draw.line(screen, 'black', (x1, y1), (x1, y1 + a), 3)
        y1 += a
        if self.walls[5]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 + hei), 3)
        x1 = x1 - half
        y1 = y1 + hei
        if self.walls[4]:
            pg.draw.line(screen, 'black', (x1, y1), (x1 - half, y1 - hei), 3)
        x1 = x1 - half
        y1 = y1 - hei
        if self.walls[0]:
            pg.draw.line(screen, 'black', (x1, y1), (x1, y1 - a), 3)

    def choice_to_go_first_half(self, grid):  # выбор следующей клетки для верхней половины поля, расширяющейся к низу
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

    def choice_to_go_second_half(self, grid):  # выбор следующей клетки для нижней половины поля, сужающейся к низу
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

    def choice_to_go_center(self, grid):  # выбор следующей клетки для центрального ряда
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


def red_dots(grid):  # рисует красные точки, которые обозначают непосещенность шестиугольника во время генерации
    for i in range(len(grid)):
        h = grid[i]
        if not h.visited:
            pg.draw.circle(screen, (196, 17, 74), (h.x + half, h.y + 0.5 * a), a // 3)


def true_false_cells_first_half(now, next):  # отмечает наличие стен для верхней половины поля
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


def true_false_cells_second_half(now, next):  # отмечает наличие стен для нижней половины поля
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


def true_false_cells_center(now, next):  # отмечает наличие стен для центрального ряда
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


def paint_hexagons():  # рисует все шестиугольники
    for i in range(len(grid)):
        grid[i].paint()


queue = deque()
usertext = ''
base_font = pg.font.Font(None, 300)
base_font2 = pg.font.Font(None, 80)
input_text = pg.Rect(550, 300, 0, 200)
game = False
right_input = False
final_input = 'NO'
typing = False
t1 = base_font2.render('', 1, GREEN)
t2 = base_font2.render('', 1, GREEN)
final_scene = False

while True:  # игровой цикл
    screen.fill(GREEN)

    for i in pg.event.get():  # обработка событий
        if i.type == pg.QUIT:
            exit()
        if not final_scene:
            if i.type == pg.KEYDOWN:
                if not game:  # все под этим условием нужно для ввода уровня
                    if i.key == pg.K_BACKSPACE:
                        usertext = usertext[:-1]
                        t1 = base_font2.render('', 1, GREEN)
                        typing = False

                    else:
                        if ((i.key == pg.K_1 or i.key == pg.K_2 or i.key == pg.K_3 or i.key == pg.K_4
                             or i.key == pg.K_5) and len(usertext) <= 0):
                            usertext += i.unicode
                            typing = True
                            t1 = base_font2.render('нажмите ENTER', 1, GREEN)
                        if i.key == pg.K_RETURN and len(usertext) == 1:
                            final_input = int(usertext)
                            game = True
                            usertext = ''
                            t1 = base_font2.render('', 1, GREEN)
                            t = base_font2.render('', 1, GREEN)
                            flag = final_input

                            if flag == 1:
                                a = 60
                                count_row = 5
                                rows = 4
                                center_start = 27
                                center_finish = 35
                                grid = [-1 for i in range(61)]
                            elif flag == 2:
                                a = 42
                                count_row = 6
                                rows = 8
                                center_start = 52
                                center_finish = 63
                                grid = [-1 for i in range(114)]
                            elif flag == 3:
                                a = 32
                                count_row = 7
                                rows = 12
                                center_start = 85
                                center_finish = 99
                                grid = [-1 for i in range(183)]
                            elif flag == 4:
                                a = 26
                                count_row = 9
                                rows = 16
                                center_start = 136
                                center_finish = 154
                                grid = [-1 for i in range(289)]
                            elif flag == 5:
                                a = 18
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

                            coordinates = []
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
                                        coordinates.append((int(x_paint), int(y_paint)))
                                    else:
                                        grid[i] = Hexagon(x_paint, y_paint, i + 1, row_in_grid, j + 1, count_row - 1)
                                        coordinates.append((int(x_paint), int(y_paint)))
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

                            x = grid[0].x
                            y = grid[0].y
                            grid[0].visited = True

                else:  # перемещение кружка при прохождении лабиринта
                    if i.type == pg.KEYDOWN:
                        if i.key == pg.K_e and (int(x + half), int(y - 1.5 * a)) in coordinates:
                            if not grid[coordinates.index((int(x), int(y)))].walls[2]:
                                x += half
                                y -= 1.5 * a

                        if i.key == pg.K_d and (int(x + half * 2), int(y)) in coordinates:
                            if not grid[coordinates.index((int(x), int(y)))].walls[1]:
                                x += half * 2
                        if i.key == pg.K_x and (int(x + half), int(y + 1.5 * a)) in coordinates:
                            if not grid[coordinates.index((int(x), int(y)))].walls[5]:
                                x += half
                                y += 1.5 * a
                        if i.key == pg.K_z and (int(x - half), int(y + 1.5 * a)) in coordinates:
                            if not grid[coordinates.index((int(x), int(y)))].walls[4]:
                                x -= half
                                y += 1.5 * a
                        if i.key == pg.K_a and (int(x - half * 2), int(y)) in coordinates:
                            if not grid[coordinates.index((int(x), int(y)))].walls[0]:
                                x -= half * 2
                        if i.key == pg.K_w and (int(x - half), int(y - 1.5 * a)) in coordinates:
                            if not grid[coordinates.index((int(x), int(y)))].walls[3]:
                                x -= half
                                y -= 1.5 * a
                        if int(x) == int(coordinates[-1][0]) and int(y) == int(coordinates[-1][1]):
                            final_scene = True

        else:  # для финального экрана
            if (i.type == pg.MOUSEBUTTONDOWN and 200 <= pg.mouse.get_pos()[0] <= 500
                    and 450 <= pg.mouse.get_pos()[1] <= 550):
                # сброс параметров для продолжения игры
                game = False
                final_scene = False
                typing = True
                x = grid[0].x
                y = grid[0].y
                grid = []
                queue = deque()
                usertext = ''
                base_font = pg.font.Font(None, 300)
                base_font2 = pg.font.Font(None, 80)
                input_text = pg.Rect(550, 300, 0, 200)
                right_input = False
                final_input = 'NO'
                t1 = base_font2.render('', 1, GREEN)
                t2 = base_font2.render('', 1, GREEN)
            elif (i.type == pg.MOUSEBUTTONDOWN and 700 <= pg.mouse.get_pos()[0] <= 1000
                  and 450 <= pg.mouse.get_pos()[1] <= 550):
                exit()

    if not final_scene:
        if not game:  # для ввода уровня
            if typing and len(usertext) == 1:
                pg.draw.rect(screen, 'white', (370, 600, 450, 60), 0)
                pg.draw.rect(screen, 'white', input_text, 0)
            txt = base_font.render(usertext, True, GREEN)
            screen.blit(txt, (input_text.x + 5, input_text.y + 5))
            input_text.w = 120
            pg.draw.rect(screen, 'white', (50, 200, 1100, 60))
            t = base_font2.render('введите уровень сложности от 1 до 5', 1, GREEN)
            screen.blit(t, (80, 200))
            screen.blit(t1, (370, 600))
            lab = pg.image.load('images/надпись.PNG')
            lab = pg.transform.scale(
                lab, (lab.get_width() // 4,
                      lab.get_height() // 4))
            dog_rect = lab.get_rect(center=(600, 100))
            screen.blit(lab, dog_rect)
        if game:  # для игрового процесса
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
            paint_hexagons()
            pg.draw.rect(screen, 'black', (cell_now.x, cell_now.y, 2 * half, a))
            red_dots(grid)
            pg.draw.rect(screen, GREEN, (coordinates[0][0], coordinates[0][1], 2 * half, a))
            pg.draw.circle(screen, 'pink', (x + half, y + 0.5 * a), (a // 2))
            pg.draw.circle(screen, 'red', (coordinates[-1][0] + half, coordinates[-1][1] + 0.5 * a), (a // 2))

    else:  # для финального кадра с кнопками и надписью
        pg.draw.rect(screen, 'white', (200, 450, 300, 100))
        pg.draw.rect(screen, 'white', (700, 450, 300, 100))
        f1 = base_font2.render('заново', 1, GREEN)
        screen.blit(f1, (250, 475))
        f1 = base_font2.render('выйти', 1, GREEN)
        screen.blit(f1, (765, 475))
        n1 = pg.image.load('images/надпись_финал.PNG')
        n1 = pg.transform.scale(
            n1, (n1.get_width() // 4.5,
                 n1.get_height() // 4.5))
        n1_rect = n1.get_rect(center=(600, 200))
        screen.blit(n1, n1_rect)
    pg.display.flip()
    time.tick(100)