import pygame
import random
import time

pygame.init()


height, width = 600, 500
screen = pygame.display.set_mode((height, width))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
color = RED, BLACK
run = True
clock = pygame.time.Clock()
FPS = 30
class Ring:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = random.choice(color)
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 8)

while run:
    ring = Ring(46, 61, 50, 50, color)
    ring.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
    pygame.display.update()