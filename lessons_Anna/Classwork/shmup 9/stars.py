import pygame
from color import *

pygame.init()

class Stars(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.unlocked = False
        self.stars_not = pygame.image.load("image_shmup/not_complete_stars.png")
        self.stars = pygame.image.load("image_shmup/complete_stars.png")
        self.image = self.stars_not
        self.rect = self.image.get_rect(center=(x, y))
    def circle_draw(self, window):
        window.blit(self.image, self.rect)
    def update(self):
        self.image = self.stars if self.unlocked else self.stars_not

