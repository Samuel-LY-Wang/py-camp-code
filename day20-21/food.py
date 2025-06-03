from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5) #halves the shape, does not assign size
        self.color("red")
        self.move()
    def move(self):
        self.teleport(20*random.randint(-14,13)+10, 20*random.randint(-14, 13)+10)