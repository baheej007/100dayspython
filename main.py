from turtle import Turtle,Screen
from traffcarmanager import CarManager
from traffplayer import Player
from traffscoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t=Player()
screen.listen()
screen.onkey(t.up,"Up")
screen.onkey(t.down,"Down")





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    car.move()

    if t.distance(car)<4:
        game_is_on=False
























screen.exitonclick()
