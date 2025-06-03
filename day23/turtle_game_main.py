#Crossy Road ripoff
from turtle import *
from random import randint
from player import Player
from level import Level
from car import CarSpawner
import time

STARTPOS=350
MAX_SCORE=10

#screen setup
s=Screen()
s.setup(height=600,width=600) #square screen ideal here rather than 640x480 typically used
s.bgcolor("white")
s.title("Crossy Road but with a turtle")
s.listen()
s.colormode(255)

#object setup
p=Player()
l=Level()
c=CarSpawner()

#movement code
s.onkey(p.up, "Up")
s.onkey(p.down, "Down")
s.onkey(p.left, "Left")
s.onkey(p.right, "Right")
s.onkey(p.up, "w")
s.onkey(p.down, "s")
s.onkey(p.left, "a")
s.onkey(p.right, "d")

game_running = True

while game_running:
    time.sleep(0.05)
    #detect if turtle has hit car

    #detect if turtle hit edge
    if p.y >= 290:
        p.reinit()
        l.level += 1
        l.update()
        c.clear()
        #move to next level

s.exitonclick()