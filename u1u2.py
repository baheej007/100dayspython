from turtle import Screen, Turtle

screen=Screen()
class move(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(pos)
        self.penup()
        self.color("white")
    def up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 50)


