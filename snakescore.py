import turtle
from turtle import Turtle

class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()

        self.hideturtle()
    def update(self):
        self.write(f"score:{self.score}", align="center", font=("Arial", 15, "bold"))
    def add(self):
        self.score=self.score+1
        self.clear()
        self.update()
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write( "GAME OVER", align="center", font=("Arial", 15, "bold"))
        self.goto(0,-50)
        self.write(f"TOTAL SCORE:{self.score}", align="center", font=("Arial", 15, "bold"))
