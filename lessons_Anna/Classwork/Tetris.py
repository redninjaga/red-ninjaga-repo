import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_SIZE = 25
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Фигуры Тетриса и их цвета
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[1, 1, 1],
     [0, 0, 1]],
    [[1, 1, 1],
     [1, 0, 0]]
]

SHAPES_COLORS = [CYAN, YELLOW, GREEN, RED, BLUE, ORANGE, MAGENTA]

# Основной экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тетрис")

# Генератор случайных чисел
random.seed()

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

def draw_shape(shape, color, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                pygame.draw.rect(screen, color, (x + col * GRID_SIZE, y + row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def check_collision(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT or board[y + row][x + col]:
                    return True
    return False

def rotate(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

def remove_row(board, row):
    for y in range(row, 0, -1):
        for x in range(GRID_WIDTH):
            board[y][x] = board[y - 1][x]
    for x in range(GRID_WIDTH):
        board[0][x] = 0
fon = pygame.font.SysFont(None, 36)
def main():
    board = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_shape = random.choice(SHAPES)
    current_color = random.choice(SHAPES_COLORS)
    shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0
    score = 0
    fall_time = 0
    fall_speed = 0.3

    clock = pygame.time.Clock()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, current_shape, shape_x - 1, shape_y):
                        shape_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, current_shape, shape_x + 1, shape_y):
                        shape_x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, current_shape, shape_x, shape_y + 1):
                        shape_y += 1
                elif event.key == pygame.K_UP:
                    rotated_shape = rotate(current_shape)
                    if not check_collision(board, rotated_shape, shape_x, shape_y):
                        current_shape = rotated_shape

        screen.fill(BLACK)
        draw_grid()

        if not check_collision(board, current_shape, shape_x, shape_y + 1):
            fall_time += clock.get_rawtime()
            if fall_time > fall_speed * 75:
                shape_y += 1
                fall_time = 0
        else:
            for row in range(len(current_shape)):
                for col in range(len(current_shape[row])):
                    if current_shape[row][col]:
                        board[shape_y + row][shape_x + col] = current_color
            for row in range(GRID_HEIGHT):
                if all(board[row]):
                    remove_row(board, row)
                    score += 10

            current_shape = random.choice(SHAPES)
            current_color = random.choice(SHAPES_COLORS)
            shape_x, shape_y = GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0

            if check_collision(board, current_shape, shape_x, shape_y):
                game_over = True

        draw_shape(current_shape, current_color, shape_x * GRID_SIZE, shape_y * GRID_SIZE)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]:
                    pygame.draw.rect(screen, board[row][col], (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        score_text = fon.render("score:" + str(score), True, RED)
        screen.blit(score_text, (10, 10))
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    print(f"Игра окончена. Ваш счет: {score}")

if __name__ == "__main__":
    main()