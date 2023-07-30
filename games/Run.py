import pygame
import random

pygame.init()
height, width = 800, 800
window = pygame.display.set_mode((height, width))
bg_color = (30, 100, 17)
x, y = 50, 50

Left = False
Right = False
Up = False
Down = False

speed = 2
score = 0
obstacles = []
number_obstacles = 10
obstacles_width = 50
obstacles_height = 50
obstacles_speed = 1

for _ in range(number_obstacles):
    obstacles_x = random.randint(0, width - obstacles_width)
    obstacles_y = random.randint(0, height - obstacles_height)
    obstacle_rect = pygame.Rect(obstacles_x, obstacles_y, obstacles_width, obstacles_height)
    obstacles.append(obstacle_rect)
run = True

while run:
    window.fill(bg_color)
    pygame.draw.rect(window, (0, 255, 10), (x, y, 50, 50))
    for obstacle_rect in obstacles:
        pygame.draw.rect(window, (57, 14, 69), obstacle_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Left = True
            elif event.key == pygame.K_RIGHT:
                Right = True
            elif event.key == pygame.K_UP:
                Up = True
            elif event.key == pygame.K_DOWN:
                Down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Left = False
            elif event.key == pygame.K_RIGHT:
                Right = False
            elif event.key == pygame.K_UP:
                Up = False
            elif event.key == pygame.K_DOWN:
                Down = False
    if Left:
        x -= speed
    if Right:
        x += speed
    if Up:
        y -= speed
    if Down:
        y += speed

    if x < 0:
        x = 0
    elif x > width - 50:
        x = width - 50
    if y < 0:
        y = 0
    elif y > height - 50:
        y = height - 50
    player_rect = pygame.Rect(x, y, 50, 50)
    for obstacle_rect in obstacles:
        if player_rect.colliderect(obstacle_rect):
            obstacle_rect.x = random.randint(0, width - obstacles_width)
            obstacle_rect.y = random.randint(0, height - obstacles_height)
    for obstacle_rect in obstacles:
        obstacle_rect.x -= obstacles_speed
        if obstacle_rect.right < 0:
            obstacle_rect.x = width
            obstacle_rect.y = random.randint(0, height - obstacles_height)
pygame.quit()
