#Racing
from turtle import *
from random import randint
t_red=Turtle(shape="turtle")
t_orange=Turtle(shape="turtle")
t_yellow=Turtle(shape="turtle")
t_green=Turtle(shape="turtle")
t_blue=Turtle(shape="turtle")
t_cyan=Turtle(shape="turtle")
t_purple=Turtle(shape="turtle")
t_red.color("red")
t_orange.color("orange")
t_yellow.color("yellow")
t_green.color("green")
t_cyan.color("cyan")
t_blue.color("blue")
t_purple.color("purple")
turtles=[t_red, t_orange, t_yellow, t_green, t_cyan, t_blue, t_purple]
s=Screen()
s.setup(640,480)
s.colormode(255)
bet=s.textinput(title="Place your bets", prompt="What turtle are you betting on?")
for i in range(7):
    turtles[i].penup()
    turtles[i].goto(-320,(i-3)*40)
raceongoing=True
while raceongoing:
    for turtle in turtles:
        turtle.forward(randint(-10,30))
    for turtle in turtles:
        if turtle.pos()[0] >= 300:
            raceongoing=False
            win_turtle=turtle.color()[0]
print(f"You bet on: {bet}, the winner was: {win_turtle}" )
if bet==win_turtle:
    print("You win!")
else:
    print("You lose.")

s.exitonclick()