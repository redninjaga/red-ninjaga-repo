from os import path
import pygame

pygame.init()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

height, width = 600, 500

game_sprites = path.join(path.dirname(__file__), 'image_shmup')
fond = pygame.font.match_font("Arial")
song_1 = pygame.mixer.Sound("music_in_shmup.mp3")
song_2 = pygame.mixer.Sound("gun_music.mp3")
song_1.set_volume(0.01)
song_1.play(-1)
song_2.set_volume(0.05)
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((width, height))

def draw_text(surf, text, color, size, x, y):
    font = pygame.font.Font(fond, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    text_rect = text_surface.get_width()
    return text_rect
