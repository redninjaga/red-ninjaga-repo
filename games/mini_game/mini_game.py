import pygame

pygame.init()
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Game")

player = pygame.image.load('draw/Redninjaga.png')
bg = pygame.image.load("draw/space.jpg")

x = 50
y = 50
speed = 5

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super.__init__()
#         self.image = pygame.image.load("draw/space.jpg")
#
#         self.change_x = 0
#         self.change_y = 0
#
#         self.level = None
#
#     def update(self):
#         self.calc_gravity()
#
#         self.rect.x += self.change_x

# class Level(object):
#     def __init__(self):
#         self.platforms = pygame.sprite.Group()
#         self.player = player
#
#         self.background = None
#
#     def update(self, screen):
#         screen.blit(bg)

clock = pygame.time.Clock()
run = True
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    win.blit(bg, (0, 0))
    win.blit(player, (x, y))
    pygame.display.update()
pygame.quit()