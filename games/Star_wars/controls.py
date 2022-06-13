import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
        #     elif event.key == pygame.K_SPACE:
        #         new_bullet = Bullet(screen, gun)
        #         bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False
# def update(bg_color, screen, gun, inos, bullets):
#     screen.fill(bg_color)
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#     gun.output()
#     inos.draw(screen)
#     pygame.display.flip()
# def update_bullets(screen, inos, bullets):
#     bullets.update()
#     for bullets in bullets.copy():
#         if bullets.rect.bottom <= 0:
#             bullets.remove(bullets)
#     collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
#     if len(inos) == 0:
#         bullets.empty()
#         create_army(screen, inos)
# def gun_kill(stats, screen, gun, inos, bullets):
#     stats.guns_left -= 1
#     inos.empty()
#     bullets.empty()
#     create_army(screen, inos)
#     gun.create_gun()
#     time.sleep()
# def update_inos(stats, screen, gun, inos, bullets):
#     inos.update()
#     if pygame.sprite.spritecollideany(gun, inos):
#         gun_kill(stats, screen, gun, inos, bullets)
# def inos_check(stats, screen, gun, inos, bullets):
#     screen_rect = screen.get.rect()
#     for ino in inos.sprites():
#         if ino.rect.bottom >= screen_rect.bottom:
#             gun_kill(stats, screen, gun, inos, bullets)
#             break
# def create_army(screen, inos):
#     ino = Ino(screen)
#     ino_width = ino.rect.width
#     number_ino_x = int((700 - 2 * ino_width) / ino_width)
#     ino_height = ino.rect.height
#     number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)
#     for row_number in range(number_ino_y):
#         for ino_number in range(number_ino_x):
#             ino = Ino(screen)
#             ino.x = ino_width + ino_width * ino_number
#         ino.rect.x = ino.x
#         ino.rect.y = ino.rect.height + 2 * ino.rect.height * row_number
#         # inos.add(ino)