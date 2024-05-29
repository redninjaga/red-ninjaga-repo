import pygame
from os import path
from color import *

pygame.init()

height, width = 600, 500
health_img = pygame.image.load(path.join(game_sprites, "Hilka.png"))

class Health(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'hilka'
        self.image = health_img
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = 10
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.kill()
