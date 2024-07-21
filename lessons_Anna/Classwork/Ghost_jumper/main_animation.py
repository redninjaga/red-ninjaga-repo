import pygame

clock = pygame.time.Clock()

pygame.init()

window = pygame.display.set_mode((600, 310))
player = pygame.image.load("charters_3.png").convert_alpha()
bg = pygame.image.load('bg.png').convert()
black = (0, 0, 0)
player_speed = 5
player_x, player_y = 100, 250
is_jump = True
player_jump = 7
Ghost_x = 610
score = 0
win_font = pygame.font.Font(None, 40)
win_text = win_font.render(f"score {score}", True, black)
heart = pygame.image.load("Score.png").convert_alpha()
heart_number = 3
run_right = [pygame.image.load("charters_3.png").convert_alpha(),
             pygame.image.load("charters_2.png").convert_alpha(),
             pygame.image.load("charters_3.png").convert_alpha(),
             pygame.image.load("charters_1.png").convert_alpha()
]
run_left = [pygame.image.load("charters_ringht_2.png").convert_alpha(),
             pygame.image.load("charters_ringht_1.png").convert_alpha(),
             pygame.image.load("charters_ringht_2.png").convert_alpha(),
             pygame.image.load("charters_ringht_3.png").convert_alpha()
]
Ghost = pygame.image.load("Ghost.png").convert_alpha()
Ghost_list = []
list = 0
bg_x = 0
run = True
Ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(Ghost_timer, 3000)
while run:
    window.blit(bg, (bg_x, 0))
    window.blit(bg, (bg_x + 600, 0))
    window.blit(bg, (bg_x - 600, 0))
    window.blit(Ghost, (Ghost_x, 260))
    window.blit(heart, (0, 0))
    window.blit(heart, (30, 0))
    window.blit(heart, (60, 0))
    window.blit(win_text, (480, 0))
    win_text = win_font.render(f"score {score}", True, black)
    player_rect = run_left[0].get_rect(topleft=(player_x, player_y))

    if Ghost_list:
        i = 0
        while i < len(Ghost_list):
            ell = Ghost_list[i]
            window.blit(Ghost, ell)
            ell.x -= 10
            if ell.x == 0:
                score += 1

            if player_rect.colliderect(ell):
                print("You lose")
                score -= 1
                heart_number -= 1
                del Ghost_list[i]
            else:
                i += 1
                if heart_number == 0:
                    run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player_x < 550:
        player_x += player_speed
    elif keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    if keys[pygame.K_LEFT]:
        window.blit(run_left[list], (player_x, player_y))
        bg_x += 2
        if bg_x == 600:
            bg_x = -600
    else:
        window.blit(run_right[list], (player_x, player_y))
        bg_x -= 2
        if bg_x == -600:
            bg_x = 0
    if is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = False
    else:
        if player_jump >= -7:
            if player_jump > 0:
                player_y -= (player_jump ** 2) / 2
            else:
                player_y += (player_jump ** 2) / 2
            player_jump -= 1
        else:
            is_jump = True
            player_jump = 7
    if list == 3:
        list = 0
    else:
        list += 1
    bg_x -= 2
    if bg_x == -600:
        bg_x = 0
    Ghost_x -= 10
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == Ghost_timer:
            Ghost_list.append(Ghost.get_rect(topleft=(610, 260)))
    clock.tick(30)
