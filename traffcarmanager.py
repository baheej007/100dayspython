from turtle import Turtle, Screen
import random

screen=Screen()

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 80
MOVE_INCREMENT = 10
screen.tracer(0)
yval=[]
for i in range(-200,250,50):
    yval.append(i)



cars=[]
jk=300

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        global jk
        self.hideturtle()
        new = Turtle("square")
        new.penup()
        new.shapesize(3,3)
        y=random.choice(yval)
        new.goto(jk,y)
        new.backward(40)
        new.speed("normal")
        jk+=100



        new.color(random.choice(COLORS))
        cars.append((new,y))

    def move(self):
        for car in cars:
            car[0].backward(13)





