from turtle import *

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.teleport(-290, 250)
        self.level = 1
        self.update()
    def update(self):
        self.clear()
        update_txt = "Level: "+str(self.level)
        self.write(update_txt, align="left", font=("Sans Serif", 20, "normal"))