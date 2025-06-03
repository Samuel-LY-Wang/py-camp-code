#Snake
from turtle import *
from random import randint
import time

STARTPOS=350
MAX_SCORE=10

s=Screen()
s.setup(height=600,width=600) #square screen ideal here rather than 640x480 typically used
s.bgcolor("white")
s.title("Crossy Road but with a turtle")
s.listen()
s.colormode(255)

game_running = True

while game_running:
    time.sleep(0.05)
    #do something

s.exitonclick()