import pygame
import time
import random
from color import *

pygame.init()

meteor_img = []
meteor_list = ["meteor_pro228.png", "meteor.png"]

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_org = random.choice(meteor_img)
#       self.image_org.set_colorkey(BLACK)
        self.image = self.image_org.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(1, 10)
        self.speed_x = random.randrange(-2, 2)
        self.rot = 0
        self.rot_speed = random.randrange(-10, 10)
        self.last_update = pygame.time.get_ticks()
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_org, self.rot)
            center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.width = random.randrange(33, 50)
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 10)