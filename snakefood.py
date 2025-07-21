import random
from turtle import Turtle,Screen
from snakeclass import snakec
import random
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-280,280),random.randint(-280,280))

    def ref(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))