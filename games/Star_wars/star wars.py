import pygame, sys, controls
from gun import Gun
# import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Star wars")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    clock = pygame.time.Clock()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, inos, sc, bullets, stats)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
            clock.tick()
            pygame.display.set_caption(f'Star_wars. FPS: {clock.get_fps() :.0f}')
run()