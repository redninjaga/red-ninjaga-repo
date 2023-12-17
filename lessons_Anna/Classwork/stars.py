import pygame
import random

pygame.init()

h, w = 600, 500
screen = pygame.display.set_mode((h, w))
bg = (0, 0, 0)

def draw(screen, x, y):
    stars_color = (0, 100, 0)
    pygame.draw.circle(screen, stars_color, (x, y), 2)
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(bg)
        random_number = random.randint(10, 20)
        for _ in range(random_number):
            x = random.randint(0, w)
            y = random.randint(0, h)
            draw(screen, x, y)
        pygame.display.flip()
        pygame.time.delay(500)
    pygame.quit()

if __name__ == "__main__":
    main()
