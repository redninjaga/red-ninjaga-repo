from configt import *
from player import Player
from functions import *

display = pygame.display.set_mode((width, height))# задаём высоту и длину окно в игре
clock = pygame.time.Clock()# Время в игре
player = Player()# персонаж в игре

while True:# работает всегда
    pygame.display.set_caption(f'3D_game. FPS: {clock.get_fps() :.0f}')# выводим на окно игры FPS
    # закрываем окно или экран игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
             # закрываем окно или экран игры
    player.delta = delta_time()
    player.move()# игрока движения
    display.fill((0, 0, 0))# цвет фона игры

    pygame.draw.rect(display, (48, 110, 172), (0, 0, width, half_height - player.hor_a))# создаём небо
    pygame.draw.rect(display, (185, 175, 170), (0, half_height - player.hor_a, width, half_height + player.hor_a))# создаём пол

    ray_casting(display, player)# разпределение лучей

    # [pygame.draw.rect(display, pygame.Color("gray"), (x, y, block_size, block_size), 1)for x, y in block_map]# прорисовуем блоки
    # pygame.draw.circle(display, pygame.Color("Yellow"), (player.x, player.y), 10)# задаём персонажу цвет, корды

    # ray_size = width# лучик
    # toX = ray_size * cos(player.angle) + player.x# Выщитывание углов
    # toY = ray_size * sin(player.angle) + player.y# Выщитывание углов
    # pygame.draw.line(display, pygame.Color("Red"), (player.x, player.y), (toX, toY))# Рисуем лучь

    clock.tick(0)# еденицы в плане секунд
    pygame.display.flip()
