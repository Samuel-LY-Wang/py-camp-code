#Pong
from turtle import *
from random import randint
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTPOS=350
MAX_SCORE=10

s=Screen()
s.setup(height=600,width=800)
s.bgcolor("black")
s.title("Pong")
p1=Paddle(-STARTPOS, 0)
p2=Paddle(STARTPOS, 0)
b=Ball()
score=Scoreboard()
s.listen()
s.colormode(255)

def paddle_up():
    p1.y = min(p1.y+p1.move_speed,300-p1.h/2)
    p1.draw(p1.x,p1.y)
def paddle_down():
    p1.y = max(p1.y-p1.move_speed,-300+p1.h/2)
    p1.draw(p1.x,p1.y)

def paddle_2_up():
    p2.y = min(p2.y+p2.move_speed,300-p2.h/2)
    p2.draw(p2.x,p2.y)
def paddle_2_down():
    p2.y = max(p2.y-p2.move_speed,-300+p2.h/2)
    p2.draw(p2.x,p2.y)
def new_point():
    score.update()
    b.x=0
    b.y=0
    b.reinit()
    time.sleep(0.5)

s.onkey(paddle_up, "Up")
s.onkey(paddle_down, "Down")
s.onkey(paddle_2_up, "w")
s.onkey(paddle_2_down, "s")

game_running = True

while game_running:
    time.sleep(0.05)
    b.move()
    if (abs(b.y) >= 280):
        b.reflect_off_wall()
    if (b.x >= 320 and abs(b.y-p2.y) <= 50):
        b.reflect_off_paddle()
    if (b.x <= -320 and abs(b.y-p1.y) <= 50):
        b.reflect_off_paddle()
    if (b.x >= 390):
        score.score[0] += 1
        new_point()
        if (score.score[0] == MAX_SCORE):
            game_running = False
    if (b.x <= -390):
        score.score[1] += 1
        new_point()
        if (score.score[1] == MAX_SCORE):
            game_running = False
winner=Turtle()
winner.hideturtle()
winner.color("white")
winner.penup()
winner.goto(0,0)
if score.score[0] == MAX_SCORE:
    winner.write("Left player wins", align="center", font=("Times New Roman", 60, "normal"))
else:
    winner.write("Right player wins", align="center", font=("Times New Roman", 60, "normal"))

s.exitonclick()