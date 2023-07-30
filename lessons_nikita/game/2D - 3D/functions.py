from configt import *
from player import Player
import pygame
import time
from math import *

cur_time = time.time_ns()
# последущего кадра в нансек
def delta_time():
    global cur_time# глобальноя переменая текущего времени
    delta = (time.time_ns() - cur_time) / 1000000000# разница времени последующего кадра и текущего в наносек
    cur_time = time.time_ns()# время последущего кадра становится текущем временем
    return delta# получаем delta
# позицыя блоков
def ray_casting(display, player):
    in_block_pos = {'left': player.x - player.x // block_size * block_size,
                    'top': player.y - player.y // block_size * block_size,
                    'right': block_size - (player.x - player.x // block_size * block_size),
                    'bottom': block_size - (player.y - player.y // block_size * block_size)}
    # позиция блоков

# невидем через блоки
    for ray in range(num_rays):
        cur_angle = player.angle - half_FOV + delta_ray * ray# выщитывание угла
        cos_a, sin_a = cos(cur_angle), sin(cur_angle)# Выщитываем углы
        vd, hd = 0, 0# Переменые вертикали, горизонтали

# вертикали
        for dep in range(max_depth):
            if cos_a > 0:
                vd = in_block_pos['right'] / cos_a + block_size / cos_a * dep + 1
            elif cos_a < 0:
                vd = in_block_pos['left'] / -cos_a + block_size / -cos_a * dep + 1
            x, y = vd * cos_a + player.x, vd * sin_a + player.y
            fixed_x, fixed_y = x // block_size * block_size, y // block_size * block_size
            if (fixed_x, fixed_y) in block_map:
                break
# вертикали
# горизонталь
        for dep in range(max_depth):
            if sin_a > 0:
                hd = in_block_pos['bottom'] / sin_a + block_size / sin_a * dep + 1# чтобы двигались лучи с игроком в низ
            elif sin_a < 0:
                hd = in_block_pos['top'] / -sin_a + block_size / -sin_a * dep + 1# чтобы двигались лучи с игроком в верх
            x, y = hd * cos_a + player.x, hd * sin_a + player.y
            fixed_x, fixed_y = x // block_size * block_size, y // block_size * block_size
            if (fixed_x, fixed_y) in block_map:
                break
# горизонтали
# невидем через блоки
        ray_size = min(vd, hd ) * depth_coeff# лучик
        ray_size *= cos(player.angle - cur_angle)
        height_c = coefficient / (ray_size + 0.0001)#
        c = 255 / (1 + ray_size ** 2 * 0.000005)# создаём затемнение блока
        color = (c, c, c)
        pygame.draw.rect(display, color, (ray * scale, (half_height - height_c // 2) - player.hor_a, scale, height_c))# закрашываем обекты в 3D
        # toX = ray_size * cos(cur_angle) + player.x  # Выщитывание углов
        # toY = ray_size * sin(cur_angle) + player.y  # Выщитывание углов
        # pygame.draw.line(display, pygame.Color("Red"), (player.x, player.y), (toX, toY))  # Рисуем лучь
# невидем через блоки

