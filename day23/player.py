from turtle import *

MIN_X=-290
MAX_X=290
MIN_Y=-290
MAX_Y=290

def clamp(num, minima, maxima):
    #returns the number, but with a specified max and min
    return min(maxima, max(minima, num))

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.reinit()
    def reinit(self):
        self.x=0
        self.y=-250
        self.teleport(self.x,self.y)
    def move(self):
        self.goto(self.x, self.y)
    def up(self):
        self.setheading(90)
        self.y += 10
        self.move()
    def down(self):
        self.setheading(270)
        self.y = clamp(self.y-10, MIN_Y, MAX_Y)
        self.move()
    def left(self):
        self.setheading(180)
        self.x = clamp(self.x-10, MIN_X, MAX_X)
        self.move()
    def right(self):
        self.setheading(0)
        self.x = clamp(self.x+10, MIN_X, MAX_X)
        self.move()