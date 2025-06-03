from turtle import *
import time

SQUARE_SIZE=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.refresh_rate=0.1
        self.last_input=0
    def create_snake(self):
        for i in range(3):
            self.add_segment(-SQUARE_SIZE*i-SQUARE_SIZE/2,-SQUARE_SIZE/2)
    def add_segment(self, posx, posy):
        new_seg=Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.teleport(posx, posy)
        self.segments.append(new_seg)
    def move(self):
        for i in range (len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(SQUARE_SIZE)
    def left(self):
        if time.time()-self.last_input >= self.refresh_rate:
            self.head.right(90)
            self.last_input=time.time()
    def right(self):
        if time.time()-self.last_input >= self.refresh_rate:
            self.head.left(90)
            self.last_input=time.time()
    def grow(self):
        self.add_segment(self.segments[-1].pos()[0], self.segments[-1].pos()[1])