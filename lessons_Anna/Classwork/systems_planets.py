import pygame
import random

pygame.init()

h, w = 800, 600

screen = pygame.display.set_mode((h, w))
bg = (0, 0, 0)
planets_color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def draw(screen, x, y):
    stars_color = (255, 255, 255)
    pygame.draw.circle(screen, stars_color, (x, y), 2)
def draw_planets(screen, x, y, color, size):
    pygame.draw.circle(screen, color, (x, y), 15)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(bg)
        random_number_stars = random.randint(10, 20)
        random_number_planets = random.randint(3, 5)
        for _ in range(random_number_stars):
            x = random.randint(0, w)
            y = random.randint(0, h)
            draw(screen, x, y)
        for _ in range(random_number_planets):
            x = random.randint(0, w)
            y = random.randint(0, h)
            color = random.choice(planets_color)
            size = random.randint(20, 50)
            draw_planets(screen, x, y, color, size)
        pygame.display.flip()
        pygame.time.delay(500)
    pygame.quit()
if __name__ == "__main__":
    main()
