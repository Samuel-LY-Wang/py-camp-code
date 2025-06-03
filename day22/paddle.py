from turtle import *

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.move_speed=20
        self.w=20.0
        self.h=100.0
        self.x=x
        self.y=y
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(self.h/20,self.w/20)
        self.teleport(self.x,self.y)
    def draw(self, x, y):
        self.goto(x,y)
        pass