from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=700)
user_bet = screen.textinput(title="Make a bet!!", prompt="Choose your turtle: ")


all_turtles = []
is_race_on = False
colors = ["red", "orange", "green", "purple", "yellow", "blue"]
y_axis = [-70, -40, -10, 20, 50, 80]


for i in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-330.0, y=y_axis[i])
    all_turtles.append(timmy)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 320:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU WON!!!")
            else:
                print("You NOOB U LOST")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
