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
        self.click = True
        self.click_money = 0

        self.plane_rect = pygame.Rect(x, y + 120, 100, 30)

    def check_click(self, mouse_pos, mouse_click, money):
        if self.plane_rect.collidepoint(mouse_pos):
            if mouse_click[0] and money >= self.price:
                self.click = False
                self.click_money = 1
                return self.price
        return 0


    def draw_btn(self):
        if self.click:
            draw_text(screen, f"{self.price}", WHITE, 35, self.x+45, (height - 125))
            self.plane_button = pygame.draw.rect(screen, WHITE, self.plane_rect)
            draw_text(screen, "buy", "gold", 30, self.plane_button.centerx, self.plane_button.centery - 20)
            return 0
        return 1

    def update(self):
        screen.blit(self.image, (self.x, self.y))

