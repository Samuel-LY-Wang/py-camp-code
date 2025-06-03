from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.teleport(0,270)
        self.score=0
        string="Score: "+str(self.score)
        self.write(string, align="center", font=("Times New Roman", 20, "normal"))
    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 36, "normal"))
    def display(self):
        self.clear()
        string="Score: "+str(self.score)
        self.write(string, align="center", font=("Times New Roman", 20, "normal"))