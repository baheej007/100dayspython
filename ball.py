from turtle import Turtle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.8,.8)
        self.color("red")
        self.xmov=2
        self.ymov=2

    def move(self):
        self.goto(self.xcor()+self.xmov,self.ycor()+self.ymov)
    def bouncey(self):
        self.ymov *=-1
    def bouncex(self):
        self.xmov *=-1

