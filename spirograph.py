import turtle
from turtle import *
import random


timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(72):
    timmy.color(random_color())
    timmy.circle(100)
    direction = timmy.heading()
    direction += 5.0
    timmy.setheading(direction)


screen = Screen()
screen.exitonclick()
