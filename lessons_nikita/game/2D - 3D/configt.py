import pygame
from math import *
height = 700#высота (целое)
width = 1200#длина (целое)
half_height = height / 2#половина высоты
half_width = width / 2#половина длины

# создаём карту
block_size = 200# размер блока
# рисуем на карте блоки
text_map = ["WWWWWWWWWWWWWWWWW",
            "W...........W",
            "WW....WWWWW.W",
            "W.........W.W",
            "W.........W.W",
            "WWW.WWWW.WWW..W",
            "W......W..WW",
            "W......WW..W",
            "W.....W....W",
            "W....WW.WWWWWW",
            "W..W..W.....W",
            "W.....W....WW..W",
            "W.W.WWWWWWWW",
            "WW.....W....WW",
            "W....WWW..WWWWW",
            "W..WWW....WWW",
            "W.W.WW....W",
            "W...W......W...W........W",
            "WWW.WW..W.W.W",
            "WWW.WWW.WWWWWW",
            "WWW.WWWWWWWWWW..WWW", ]
# рисуем на карте блоки
block_map = set()#об'явление карты
y_block_pos = 0# повысоте оси y
# проверяет блоки
for row in text_map:
    x_block_pos = 0
    for column in list(row):
        if column == "W":
            block_map.add((x_block_pos, y_block_pos))
        x_block_pos += block_size
    y_block_pos += block_size
# проверяет блоки

# разделение лучев
FOV = pi / 2
half_FOV = FOV / 2
max_depth = width // block_size
num_rays = 1200
delta_ray = FOV / (num_rays - 1)
# разделение лучев
dist = num_rays / (2 * tan(half_FOV))
coefficient = dist * block_size * 100
scale = width // num_rays
depth_coeff = 2
