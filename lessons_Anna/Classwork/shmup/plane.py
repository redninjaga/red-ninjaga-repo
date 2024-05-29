import pygame

from color import *

class Plane(pygame.sprite.Sprite):
    def __init__(self, screen, img, x, y, price, money):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.price = price
        self.money = money

        #Отрисовка каждого изображения в классе по переданным координатам
        screen.blit(self.image, (x, y))

        # Отрисовка цены каждого самолета
        draw_text(screen, f"{self.price}", WHITE, 35, x+45, (height - 125))

        self.plane_rect = pygame.Rect(x, y + 120, 100, 30)
        self.plane_button = pygame.draw.rect(screen, WHITE, self.plane_rect)
        draw_text(screen, "buy", "gold", 30, self.plane_button.centerx, self.plane_button.centery - 20)

    def check_click(self, mouse_pos, mouse_click):
        if self.plane_rect.collidepoint(mouse_pos):
            if mouse_click[0] and self.money >= self.price:
                return self.price
        return 0
