import pygame.mouse
from pygame import *

from levels import *
from enemy import *
from health import *
from stars import *
from plane import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()
#dddddddddddddddddaa da dwdddddddddddddddddddddddddda

# Создание уровней
global money
money = 0
money_image = pygame.image.load(path.join(game_sprites, "money_2.png"))
player_img_aqua = pygame.image.load(path.join(game_sprites, "player_img_aqua.png"))
player_img_brown = pygame.image.load(path.join(game_sprites, "player_img_brown.png"))
player_img_grey = pygame.image.load(path.join(game_sprites, "player_img_grey.png"))
level_select = False
level_now = 1
width_rect_1 = 222
height_rect_1 = 50
width_rect_2 = 222
height_rect_2 = 50
fond = pygame.font.match_font("Arial")
planes = [
    Plane(screen, player_img_aqua, width / 2 - (player_img_aqua.get_width()) / 2, height - 200, 100, money),
    Plane(screen, player_img_brown, width - 120, height - 200, 150, money),
    Plane(screen, player_img_grey, width - 480, height - 200, 120, money)
]


def check_boss(mobs):
    if level_now % 5 == 0:
        for mob in mobs:
            mob.speed_y = random.randrange(40, 50)
        return True
    else:
        for mob in mobs:
            mob.speed_y = random.randrange(1, 10)
        return False
        #print("radius", mob.radius)



def level_create(width_screen, width_level, distance_level, height_screen, height_level, score):
    global levels
    global lvl_score
    global star_second
    star_second = []
    lvl_score = []
    levels = []
    number = 1
    count_x = width_screen // (width_level + distance_level)
    count_y = height_screen // (height_level + distance_level * 2)
    x, y = 10, 10
    second = 10

    for i in range(count_y-1):
        for j in range(count_x):
            l = Level((x, y), number)
            x += width_level + distance_level
            number += 1
            levels.append(l)
            lvl_score.append(score)
            star_second.append(second)
            second += 5
            score += 50
        x = 10
        y += height_level + (distance_level * 2)
    levels[0].unlocked = True  # Первый уровень изначально открыт


def minuse_money(planes, money):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    temp = money
    for plane in planes:
        if plane.draw_btn() == 0:
            cost = plane.check_click(mouse_pos, mouse_click, money)
            if cost > 0 and money > temp - cost:
                print("Cost:", cost, "money", money, "temp - cost =", temp - cost)
                plane.click = False
                money -= cost
                return money
    return money


def show_window_level():
    global level_now
    global level_select
    screen.fill(BLACK)

    for level in levels:
        level.draw(screen)

    back_rect = pygame.Rect(420, 550, 70, 40)
    back_button = pygame.draw.rect(screen, WHITE, back_rect)
    draw_text(screen, "back", GREY, 30, back_button.centerx, back_button.centery - 20)

    screen.blit(money_image, (10, 562))
    draw_text(screen, str(money), "gold", 35, 60 + (money + 1) / 100, 555)

    pygame.display.flip()
    wait = True
    while wait:
        clock.tick(200)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                for i, level in enumerate(levels):
                    if level.click(ev.pos):
                        run_main(False)
                        level_now = level.number
                        level_select = True
                        wait = False
        x, y = pygame.mouse.get_pos()
        if back_rect.collidepoint((x, y)):
            if pygame.mouse.get_pressed()[0]:
                wait = False
                run_main(True)


def click_shop():
    global money
    screen.fill(BLACK)
    wait = True

    while wait:
        clock.tick(200)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        back_rect = pygame.Rect(420, 560, 70, 40)
        back_button = pygame.draw.rect(screen, WHITE, back_rect)
        draw_text(screen, "back", GREY, 30, back_button.centerx, back_button.centery - 20)
        x, y = pygame.mouse.get_pos()

        for plane in planes:
            plane.draw_btn()
            plane.update()
            if plane.plane_rect.collidepoint((x, y)):
                if pygame.mouse.get_pressed()[0] and plane.click and plane.click_money < 1:
                    plane.draw_btn()
                    money = minuse_money(planes, money)
                    buy_rect = pygame.Rect(plane.plane_rect.x, plane.plane_rect.y, 100, 30)
                    buy_button = pygame.draw.rect(screen, BLACK, buy_rect)
                    price_rect = pygame.Rect(plane.plane_rect.x, plane.plane_rect.y - 40, 100, 30)
                    price_button = pygame.draw.rect(screen, BLACK, price_rect)
                    pygame.display.update()
            elif plane.rect.collidepoint((x, y)):
                print(plane.price)
                if pygame.mouse.get_pressed()[0] and plane.click_money == 1:
                    print(plane.price)

        if back_rect.collidepoint((x, y)):
            if pygame.mouse.get_pressed()[0]:
                wait = False
                run_main(True)

        money_rect = pygame.Rect(width - 100, height - 595, 70, 40)
        money_button = pygame.draw.rect(screen, BLACK, money_rect)

        screen.blit(money_image, (width - 100, height - 595))
        draw_text(screen, str(money), "gold", 35, 450, 0)

        pygame.display.flip()


play_rect = pygame.Rect((width / 2) - (width_rect_1 / 2), 315, width_rect_1, height_rect_1)
shop_rect = pygame.Rect((width / 2) - (width_rect_2 / 2), 450, width_rect_2, height_rect_2)
play_button = pygame.draw.rect(screen, BLUE, play_rect)
shop_button = pygame.draw.rect(screen, RED, shop_rect)

draw_text(screen, "play", GREEN, 40, play_button.centerx, play_button.centery - 30)
draw_text(screen, "shop", BLUE, 40, shop_button.centerx, shop_button.centery - 25)


def run_main(running):
    screen.fill(BLACK)
    while running:
        #print("run")
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        x, y = pygame.mouse.get_pos()
        if play_rect.collidepoint((x, y)):
            play_button = pygame.draw.rect(screen, GREEN, play_rect)
            draw_text(screen, "play", BLUE, 40, play_button.centerx, play_button.centery - 30)
            if pygame.mouse.get_pressed()[0]:
                running = False
                show_window_level()

        else:
            play_button = pygame.draw.rect(screen, BLUE, play_rect)
            draw_text(screen, "play", GREEN, 40, play_button.centerx, play_button.centery - 30)
        x1, y1 = pygame.mouse.get_pos()
        if shop_rect.collidepoint((x1, y1)):
            shop_button = pygame.draw.rect(screen, RED, shop_rect)
            draw_text(screen, "shop", BLUE, 40, shop_button.centerx, shop_button.centery - 25)
            if pygame.mouse.get_pressed()[0]:
                running = False
                click_shop()
        else:
            shop_button = pygame.draw.rect(screen, BLUE, shop_rect)
            draw_text(screen, "shop", RED, 40, shop_button.centerx, shop_button.centery - 25)
        pygame.display.flip()

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


def stars_time(get_time, arr, level):
    global money
    money = money + 20
    if get_time <= star_second[level_now - 1]:
        print("3 stars")
        for x in range(3):
            levels[level_now - 1].stars[x].unlocked = True
            levels[level_now - 1].stars[x].update()

    elif get_time <= star_second[level_now - 1] + 5:
        for x in range(2):
            levels[level_now - 1].stars[x].unlocked = True
            levels[level_now - 1].stars[x].update()

    else:
        levels[level_now - 1].stars[0].unlocked = True
        levels[level_now - 1].stars[0].update()


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




laser = pygame.image.load(path.join(game_sprites, "laser.png"))
player_img = pygame.image.load(path.join(game_sprites, "player_img.png"))


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


    def shut(self):
        now = pygame.time.get_ticks()
        if now - self.last_shut > self.shut_delay:
            self.last_shut = now
            bullet = Gun(self.rect.centerx, self.rect.top)
            song_2.play()
            bullets.add(bullet)
            all_sprites.add(bullet)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.type == pygame.K_SPACE:
                        song_2.pause()

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


# stars = Stars(20, 40)
background = pygame.image.load(path.join(game_sprites, "background.png")).convert_alpha()
background_rect = background.get_rect()

group_health = pygame.sprite.Group()
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
for i in range(10):
    new_mob()
player.helth = 100

run = True

score = 0
game_over = True
points = [100, 120, 150]
money = 0
while run:
    if game_over:
        level_create(width, 40, 10, height, 50, 100)
        run_main(True)
        if level_select:
            global start_time
            start_time = time.time()
            starting_window()
            game_over = False
            all_sprites = pygame.sprite.Group()
            player = Player()
            mobs = pygame.sprite.Group()
            check_boss(mobs)
            bullets = pygame.sprite.Group()
            all_sprites.add(player)
            for i in range(10):
                new_mob()
    if score >= lvl_score[level_now - 1]:

        end_time = time.time()
        all_time = end_time - start_time
        stars_time(all_time, star_second, level_now)
        if level_now == len(levels):
            score = 0
            show_window_level()
        levels[level_now].unlocked = True
        show_window_level()
        score = 0
        player.helth = 100
        start_time = time.time()
        print(level_now)
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
        if random.random() > 0.9:
            hilka = Health(p.rect.center)
            all_sprites.add(hilka)
            group_health.add(hilka)
        all_sprites.add(anim_boom)
        score += p.radius * 8

    push = pygame.sprite.spritecollide(player, mobs, False)
    for pushs in push:
        player.helth -= pushs.radius / 2
        pushs.kill()
        anim_boom = Boom(pushs.rect.center, "sm")
        all_sprites.add(anim_boom)
        new_mob()
        if player.helth <= 0:
            score = 0
            show_window_level()
            player.helth = 100
    push = pygame.sprite.spritecollide(player, group_health, True)
    for p in push:
        if p:
            player.helth += random.randint(5, 30)
            if player.helth >= 100:
                player.helth = 100
    screen.fill(BLACK)
    screen.blit(background, background_rect)

    health_bar(screen, 5, 5, player.helth)
    if check_boss(mobs):
        draw_text(screen, str(score), BLUE, 35, width - 30, 0)
    else:
        draw_text(screen, str(score), RED, 35, width - 30, 0)
    money_txt = draw_text(screen, str(money), "gold", 35, width - 40, height - 40)
    screen.blit(money_image, ((width - 60)-money_txt, height - 32))

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
