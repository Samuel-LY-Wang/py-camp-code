from turtle import *
import time
import random

MOVE_SPEED=100
ACCEL=1.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x=0
        self.y=0
        self.vx=MOVE_SPEED
        self.vy=MOVE_SPEED*(random.random()*0.5+0.5)
        self.t=time.time()
        self.shape("square")
        self.penup()
        self.color("white")
        self.teleport(self.x,self.y)
    def move(self):
        dt=time.time()-self.t
        self.t += dt
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.goto(self.x,self.y)
    def reflect_off_wall(self):
        self.vy *= -1
    def reflect_off_paddle(self):
        self.vx *= -ACCEL
        self.vy *= ACCEL
    def reinit(self):
        self.x=0
        self.y=0
        self.vx=MOVE_SPEED
        self.vy=MOVE_SPEED*(random.random()*0.5+0.5)
        self.t=time.time()
        self.teleport(self.x,self.y)