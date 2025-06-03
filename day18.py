from turtle import *
from random import randint
def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))
t=Turtle()
t.hideturtle()
s=Screen()
s.colormode(255)
for i in range(-300, 300, 40):
    for j in range(-300, 300, 40):
        t.teleport(i, j)
        t.dot(10, random_color())
s.exitonclick()