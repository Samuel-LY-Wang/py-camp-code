from turtle import *
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=[0,0]
        self.penup()
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(str(self.score[0]), align="center", font=("Times New Roman", 80, "normal"))
        self.goto(100,200)
        self.write(str(self.score[1]), align="center", font=("Times New Roman", 80, "normal"))