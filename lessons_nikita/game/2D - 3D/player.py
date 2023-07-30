from configt import *
import pygame.key
from math import *
class Player:
    def __init__(self):
        self.x = half_width# выставляли player по центру по x
        self.y = half_height# выставляли player по центру по y
        self.angle = 0# сосдали лучь который щитает углы
        self.delta = 0# раздница во времени(после движение текущего)
        self.speed = 750# скорость игрока в пикселях
        self.hor_a = 0# скорость вращения камеры по вертикали
    def move(self):
        key = pygame.key.get_pressed()# просматриваем какая клавиша зажата
        cos_a, sin_a = cos(self.angle), sin(self.angle)# переопредилаем синус и косинус
        new_x = self.x
        new_y = self.y
        if key[pygame.K_UP]:
            self.hor_a -= 150 * self.delta * 12# скорость поворота на вверх
        if key[pygame.K_DOWN]:
            self.hor_a += 150 * self.delta * 12# скорость поворота в низ
        if key[pygame.K_LEFT]:
            self.angle -= 0.3 * self.delta * 12# скорость поворота на лево
        if key[pygame.K_RIGHT]:
            self.angle += 0.3 * self.delta * 12# скорость поворота на право
        if key[pygame.K_w]:
            new_x += cos_a * self.delta * self.speed# выщитывание настоящий скорости по оси x
            new_y += sin_a * self.delta * self.speed# выщитывание настоящый скорости по оси y
        if key[pygame.K_s]:
            new_x -= cos_a * self.delta * self.speed# выщитывание настоящий скорости по оси x
            new_y -= sin_a * self.delta * self.speed# выщитывание настоящый скорости по оси y
        if key[pygame.K_d]:
            new_y -= sin_a * self.delta * self.speed# выщитывание настоящый скорости по оси y
            new_x += cos_a * self.delta * self.speed# выщитывание настоящий скорости по оси x
        if key[pygame.K_a]:
            new_y += sin_a * self.delta * self.speed# выщитывание настоящый скорости по оси y
            new_x -= cos_a * self.delta * self.speed# выщитывание настоящий скорости по оси x
        block_x = int(new_x // block_size) * block_size
        block_y = int(new_y // block_size) * block_size
        if (block_x, block_y) not in block_map:
            self.x = new_x
            self.y = new_y

