#Snake
from turtle import *
from random import randint
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
s=Screen()
s.setup(600,600) #square screen ideal here rather than 640x480 typically used
s.bgcolor("black")
s.title("Snake")
s.tracer(0)
s.listen()
s.colormode(255)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
s.onkey(snake.left, "Right")
s.onkey(snake.right, "Left")
s.update()
game_running=True
while game_running:
    snake.move()
    time.sleep(snake.refresh_rate) #refresh rate is found in snake.py, that's how we control the speed of the game
    #detect collision with food
    if snake.head.distance(food) < 10:
        food.move()
        snake.grow()
        scoreboard.score += 1
        scoreboard.display()
    #detect collision with wall
    if (abs(snake.head.pos()[0]) >= 300 or abs(snake.head.pos()[1]) >= 300):
        game_running=False
    #detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running=False
    s.update()

scoreboard.game_over()

s.exitonclick()