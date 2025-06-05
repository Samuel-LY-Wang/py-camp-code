from turtle import *
from time import time
from datetime import datetime

FONT_SIZE=12

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.teleport(0,240)
        self.score=0
        with open("day20-21/highscore.txt", "r") as self.f:
            self.highscore=int(self.f.readline())
            self.highscore_time=str(datetime.fromtimestamp(float(self.f.readline())))[:-7]
        string="Score: "+str(self.score)+"\nHigh score: "+str(self.highscore)+"\nAchieved at: "+str(self.highscore_time)
        self.write(string, align="center", font=("Times New Roman", FONT_SIZE, "normal"))
    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.highscore_time = time()
            with open("day20-21/highscore.txt", "w") as self.f:
                self.f.write(str(self.highscore)+"\n"+str(self.highscore_time))
            self.highscore_time=str(datetime.fromtimestamp(self.highscore_time))[:-7]
        self.display()
        self.teleport(0,0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 36, "normal"))
    def display(self):
        self.clear()
        string="Score: "+str(self.score)+"\nHigh score: "+str(self.highscore)+"\nAchieved at: "+str(self.highscore_time)
        self.write(string, align="center", font=("Times New Roman", FONT_SIZE, "normal"))