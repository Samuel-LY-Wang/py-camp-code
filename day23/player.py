from turtle import *

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
        self.y -= 10
        self.move()
    def left(self):
        self.setheading(180)
        self.x -= 10
        self.move()
    def right(self):
        self.setheading(0)
        self.x += 10
        self.move()