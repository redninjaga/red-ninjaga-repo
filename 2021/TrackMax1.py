# Ваше домашнее задание: написать такую программу, чтоб чёрная черепаха всегда проигрывала

from turtle import *
from random import randint

# n = int(input('Введите кол-во беговых дорожек:\n'))
# l = int(input('Введите длину беговых дорожек:\n'))

n = 15
l = 200

x = (n - 1) * 10
y = l / 2

penup()
speed(0)
goto(-x,y)

for i in range(n):
    pendown()
    write(i)
    right(90)
    forward(l)
    backward(l)
    left(90)
    penup()
    forward(20)


red = Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(-x-20, y-20)

blue = Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.goto(-x-20, y-60)

yellow = Turtle()
yellow.shape("turtle")
yellow.color("yellow")
yellow.penup()
yellow.goto(-x-20, y-100)

green = Turtle()
green.shape("turtle")
green.color("green")
green.penup()
green.goto(-x-20, y-140)

black = Turtle()
black.shape("turtle")
black.penup()
black.goto(-x-20, y-180)

for i in range(100):
    red.forward(randint(0,10))
    blue.forward(randint(0,10))
    yellow.forward(randint(0,10))
    green.forward(randint(0,10))
    black.forward(randint(0,15)/2)