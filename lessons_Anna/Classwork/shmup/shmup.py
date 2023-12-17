import tkinter
from tkinter import *
import time
from os import path
import pygame
import random

pygame.init()

height, width = 600, 500

screen = pygame.display.set_mode((width, height))
FPS = 60
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
game_sprites = path.join(path.dirname(__file__), "image_shmup")
clock = pygame.time.Clock()
#dddddddddddddddddaa da dwdddddddddddddddddddddddddda
fond = pygame.font.match_font("Arial")

def starting_window():
    screen.blit(background, background_rect)
    draw_text(screen, "Welcome to the shmup", BLUE, 50, width / 2, height - 500)
    draw_text(screen, "Press any key for starting", BLACK, 50, width / 2, height / 2)
    draw_text(screen, "Press space for shoot", GREEN, 50, width / 2, height - 100)
    pygame.display.flip()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                running = False
def draw_text(surf, text, color, size, x, y):
    font = pygame.font.Font(fond, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def new_mob():
    enemy = Enemy()
    all_sprites.add(enemy)
    mobs.add(enemy)
def health_bar(surf, x, y, health):
    bar_length = 100
    bar_height = 10
    fell = (health / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fell_rect = pygame.Rect(x, y, fell, bar_height)
    pygame.draw.rect(surf, GREEN, fell_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
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

class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = 10
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (55, 65))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speed = 0
        self.helth = 100
        self.shut_delay = 250
        self.last_shut = pygame.time.get_ticks()
    def update(self):
        self.speed = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a] and self.rect.x > 0:
            self.speed = -8

        if key[pygame.K_d] and self.rect.x < width - self.rect.width:
            self.speed = 8
        self.rect.x += self.speed
        if key[pygame.K_SPACE]:
            self.shut()
    def shut(self):
        now = pygame.time.get_ticks()
        if now - self.last_shut > self.shut_delay:
            self.last_shut = now
            bullet = Gun(self.rect.centerx, self.rect.top)
            song_2.play()
            all_sprites.add(bullet)
            bullets.add(bullet)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.type == pygame.K_SPACE:
                        song_2.pause()
class Boom(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = animation[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(animation[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = animation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
class Health(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(heath_img)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = 10
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.kill()
all_sprites = pygame.sprite.Group()
background = pygame.image.load(path.join(game_sprites, "background.png")).convert_alpha()
background_rect = background.get_rect()
laser = pygame.image.load(path.join(game_sprites, "laser.png")).convert_alpha()
player_img = pygame.image.load(path.join(game_sprites, "player_img.png")).convert_alpha()
meteor_img = []
meteor_list = ["meteor_pro228.png", "meteor.png"]
heath_img = pygame.image.load(path.join(game_sprites, "Hilka.png")).convert_alpha()
#      ddddddddddddddddddddddddddddd
for img in meteor_list:
    meteor_img.append(pygame.image.load(path.join(game_sprites, img)).convert_alpha())
animation = {}
animation["lg"] = []
animation["sm"] = []
for x in range(9):
    file = "regularExplosion0{}.png".format(x)
    boom_img = pygame.image.load(path.join(game_sprites, file)).convert_alpha()
    img_lg = pygame.transform.scale(boom_img, (75, 75))
    animation["lg"].append(img_lg)
    img_sm = pygame.transform.scale(boom_img, (32, 32))
    animation["sm"].append(img_sm)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
for i in range(10):
    new_mob()
player.helth = 100

run = True
song_1 = pygame.mixer.Sound("music_in_shmup.mp3")
song_2 = pygame.mixer.Sound("gun_music.mp3")
song_1.set_volume(0.01)
song_1.play(-1)
song_2.set_volume(0.05)
score = 0
game_over = True
while run:
    if game_over:
        starting_window()
        game_over = False
        all_sprites = pygame.sprite.Group()
        player = Player()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        all_sprites.add(player)
        for i in range(10):
            new_mob()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.pause()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                song_2.play()
                player.shut()
    all_sprites.update()
    push = pygame.sprite.groupcollide(mobs, bullets, True, True)

    for p in push:
        new_mob()
        anim_boom = Boom(p.rect.center, "lg")
        all_sprites.add(anim_boom)
        score += p.radius / 4

    push = pygame.sprite.spritecollide(player, mobs, False)
    for pushs in push:
        player.helth -= pushs.radius / 2
        pushs.kill()
        anim_boom = Boom(pushs.rect.center, "sm")
        all_sprites.add(anim_boom)
        new_mob()
        if player.helth <= 0:
            score = 0
            game_over = True
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    health_bar(screen, 5, 5, player.helth)
    draw_text(screen, str(score), RED, 35, width - 30, 0)
    pygame.display.flip()
pygame.quit()
