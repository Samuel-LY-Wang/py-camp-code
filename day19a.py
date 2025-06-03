#Etch a Sketch
from turtle import *
t=Turtle()
s=Screen()
s.colormode(255)
s.listen()
def move_forward():
    t.forward(20)
def move_back():
    t.back(20)
def turn_left():
    t.left(20)
def turn_right():
    t.right(20)
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.onkey(clear_screen, "c")
s.onkey(move_forward, "Up")
s.onkey(move_forward, "w")
s.onkey(move_back, "Down")
s.onkey(move_back, "s")
s.onkey(turn_left, "Left")
s.onkey(turn_left, "a")
s.onkey(turn_right, "Right")
s.onkey(turn_right, "d")
s.exitonclick()
