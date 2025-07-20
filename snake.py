import turtle
from turtle import Turtle,Screen
import random
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("SNAKE AND APPLE")

fp=[]
for i in range(-280,280,5):
    fp.append(i)
f=Turtle()
f.shape("square")
f.color("red")
f.shapesize(.5,.5)
f.penup()
f.speed("fastest")
f.goto(random.choice(fp),random.choice(fp))

def



s=Turtle()
s.shape("circle")
s.color("GREEN")
s.shapesize(1,1)
s.pensize(1)
s.penup()
s.speed("slowest")

screen.listen()
def right():
    s.setheading(0)
screen.onkey(right,"d")
def left():
    s.setheading(180)
screen.onkey(left,"a")
def up():
    s.setheading(90)
screen.onkey(up,"w")
def down():
    s.setheading(270)
screen.onkey(down,"s")

move=True
while move:
    s.forward(1)
    if f.xcor()>0 and f.ycor()>0:
        if s.xcor()+1<=f.xcor() and s.ycor()+1<=f.ycor():
           f.goto(random.choice(fp),random.choice(fp))
    if f.xcor()>0 and f.ycor()>0:
        if s.xcor()+1<=f.xcor() and s.ycor()>=f.ycor():
           f.goto(random.choice(fp),random.choice(fp))
    if f.xcor()>0 and f.ycor()>0:
        if s.xcor()>=f.xcor() and s.ycor()<=f.ycor():
           f.goto(random.choice(fp),random.choice(fp))
    if f.xcor()<0 and f.ycor()<0:
        if s.xcor()>=f.xcor() and s.ycor()>=f.ycor():
           f.goto(random.choice(fp),random.choice(fp))




































screen.exitonclick()