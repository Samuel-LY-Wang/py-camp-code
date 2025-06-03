from turtle import *
from random import *

def get_random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    r_hex=hex(r)[2:]
    if len(r_hex) == 0:
        r_hex="00"
    elif len(r_hex) == 1:
        r_hex="0"+r_hex
    g_hex=hex(g)[2:]
    if len(g_hex) == 0:
        g_hex="00"
    elif len(g_hex) == 1:
        g_hex="0"+g_hex
    b_hex=hex(b)[2:]
    if len(b_hex) == 0:
        b_hex="00"
    elif len(b_hex) == 1:
        b_hex="0"+b_hex
    color="#"+r_hex+g_hex+b_hex
    return color

class CarSpawner(Turtle):
    def __init__(self):
        self.cars = []
        self.maxspeed=10.0
        self.spawn_car()
    def spawn_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(get_random_color())
        new_car.teleport(320,randint(-200,200))
        new_car.setheading(180)
        new_car.shapesize(1,2)
        self.cars.append(new_car)
    def move_cars(self):
        for car in self.cars:
            car.forward(random()*self.maxspeed)
            if car.xcor() <= -320:
                self.cars.remove(car)
    def clear_cars(self):
        for car in self.cars:
            car.clear()
            car.hideturtle()
            del(car)
            car=None
        self.cars.clear()