from turtle import Turtle,Screen

from PIL.ImageChops import screen

ob=Turtle()
ob.shape("arrow")
ob.pensize(10)

def forward():
    ob.forward(10)
def hforward():
    ob.forward(50)
def backward():
    ob.backward(10)
def right():
    nh=ob.heading()-10
    ob.setheading(nh)
def left():
    nh = ob.heading() + 10
    ob.setheading(nh)
def circle():
    ob.circle(20)
def up():
    ob.penup()
def down():
    ob.pendown()



screen=Screen()
screen.listen()
screen.onkey(forward,"w")
screen.onkey(hforward,"3")
screen.onkey(circle,"o")
screen.onkey(backward,"s")
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(up,"n")
screen.onkey(down,"m")
screen.exitonclick()
