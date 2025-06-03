#Crossy Road ripoff
#cars on average get 5% faster per level
from turtle import *
from random import randint
from player import Player
from level import Level
from car import CarSpawner
import time

#screen setup
s=Screen()
s.setup(height=600,width=600) #square screen ideal here rather than 640x480 typically used
s.bgcolor("white")
s.title("Crossy Road but with a turtle")
s.listen()
s.tracer(0)
s.colormode(255)

#object setup
p=Player()
l=Level()
c=CarSpawner()

#movement code
s.onkey(p.up, "Up")
s.onkey(p.down, "Down")
s.onkey(p.left, "Left")
s.onkey(p.right, "Right")
s.onkey(p.up, "w")
s.onkey(p.down, "s")
s.onkey(p.left, "a")
s.onkey(p.right, "d")

game_running = True
i=0

while game_running:
    time.sleep(0.05)
    #detect if turtle has hit car
    for car in c.cars:
        if (abs(car.xcor()-p.x) <= 30 and abs(car.ycor()-p.y) <= 20):
            game_running=False
    #spawn cars every 0.2 seconds to be slightly fair
    if (i % 4 == 0):
        c.spawn_car()
    c.move_cars()
    s.update()
    #detect if turtle hit edge
    if p.y >= 290:
        p.reinit()
        l.level += 1
        l.update()
        c.maxspeed *= 1.05
        c.clear_cars()
        #move to next level
    i += 1
game_over=Turtle()
game_over.hideturtle()
game_over.penup()
game_over.write("GAME OVER", align="center", font=("Arial", 60, "normal"))


s.exitonclick()