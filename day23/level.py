from turtle import *

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.teleport(-290, 290)
        self.update()
        self.level = 1
    def update(self):
        update_txt = "Level: "+self.level
        self.write(update_txt, align="left", font=("Sans Serif", 20, "normal"))