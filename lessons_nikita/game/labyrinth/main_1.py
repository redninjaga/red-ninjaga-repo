import pygame
from random import choice

res = widht, height = 1002, 702# размеры окна игры
tile = 200# размер(ы) квадрат(а, ов)
cols, rows = widht // tile, height // tile# столбы, ряды

pygame.init()
sc = pygame.display.set_mode(res)# задаём размеры окна игры res
clock = pygame.time.Clock()# время в игре

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y# координаты y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}# стенны
        self.visited = False# смотрит бот что мы прошли

    def draw_current_cell(self):
        x, y = self.x * tile, self.y * tile# координаты x, y
        pygame.draw.rect(sc, pygame.Color('lightblue'), (x + 2, y + 2, tile - 2, tile - 2))# блоки которые бот прошол

    def draw(self):
        x, y = self.x * tile, self.y * tile# координаты x, y
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('blue'), (x, y, tile, tile))# блоки которые бот прошол
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('floralwhite'), (x, y), (x + tile, y), 2)# вверхния стенна
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('floralwhite'), (x + tile, y), (x + tile, y + tile), 2)# правая стенна
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('floralwhite'), (x + tile, y + tile), (x, y + tile), 2)# нижнняя стенна
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('floralwhite'), (x, y + tile), (x, y), 2)# левая стенна

# смотрим текущию клетку
    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

# смотрим текущию клетку
#
    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False



grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []

while True:
    sc.fill(pygame.Color('darkslategray'))# цвет фонна
# выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exit()
# выход из игры

    [cell.draw() for cell in grid_cells]

    current_cell.visited = True
    current_cell.draw_current_cell()

    next_cell = current_cell.check_neighbors()
    if next_cell:
        next_cell.visited = True
        current_cell = next_cell

    pygame.display.flip()
    clock.tick(30)