import pygame, sys, controls
from gun import Gun
# import controls
from pygame.sprite import Group
# from ino import Ino
# from stats import Stats

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Star wars")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    # inos = Ino(screen)
    # controls.create_army(screen, inos)
    # stats = Stats()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets)
        # controls.update_bullets(screen, inos, bullets)
        # controls.update_inos(stats, screen, gun, inos, bullets  )

run()