import pygame
import time
from stars import *
from color import *

pygame.init()

class Level:
    def __init__(self, position, number):
        self.number = number
        self.position = position
        self.unlocked = False
        self.stars = []  # Список для хранения звезд уровня
        # Создаем 3 звезды для каждого уровня
        count = 5
        for i in range(3):
            star_x = position[0] + count # Горизонтальное смещение звезд
            star_y = position[1] + 60  # Вертикальное положение звезд ниже уровня
            self.stars.append(Stars(star_x, star_y))
            count += 15
    def draw(self, window):
        color = WHITE if self.unlocked else GREY
        pygame.draw.rect(window, color, (*self.position, 40, 50))
        font = pygame.font.SysFont("Arial", 36)
        text = font.render(f"{self.number}", True, BLACK)
        window.blit(text, (self.position[0] + 5, self.position[1]))
        for star in self.stars:
            star.circle_draw(window)
    def click(self, mouse_position):
        x, y = self.position
        if x <= mouse_position[0] <= x + 50 and y <= mouse_position[1] <= y + 50:
            return self.unlocked
        return False
