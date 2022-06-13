# 1
from tkinter import *

HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('папади')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
c.pack()

# 2
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='black')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)

# 3
SHIP_SPD = 30


def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif event.keysym == 'Right':
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)


c.bind_all('<Key>', move_ship)

# 4
from random import randint

bub_id = list()

bub_r = list()

bub_speed = list()

MIN_BUB_R = 10

MAX_BUB_R = 40

MAX_BUB_SPD = 10

GAP = 100


def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)

    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


# 5
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)


# 7
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


# 8
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]


# 9
def clean_up_bubs():
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)


# 11
from math import sqrt


def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 12
def collision():
    points = 0
    for bub in range(len(bub_id) - 1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])

            del_bubble(bub)

    return points


# 14
c.create_text(50, 30, text='TIME', fill='white')
c.create_text(150, 30, text='score', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')


def show_score(score):
    c.itemconfig(score_text, text=str(score))


def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


# 6

from time import sleep, time

BUB_CHANCE = 10
TIME_LITMIT = 30
BONUS_SCORE = 1180
score = 0
bonus = 0
end = time() + TIME_LITMIT
# create bubble
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    # 10
    clean_up_bubs()
    # 13
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LITMIT

    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

# 17
c.create_text(MID_X, MID_Y, text='конец', fill='red', font=('Helvetica', 30))
c.create_text(MID_X, MID_Y + 35, text='SCORE:' + str(score), fill='red', font=('Helvetica', 20))
c.create_text(MID_X, MID_Y + 60, text='bonus time:' + str(bonus * TIME_LITMIT), fill='red', font=('Helvetica', 20))