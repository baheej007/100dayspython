import turtle as t
import random
from turtle import Screen

tim=t.Turtle()
tim.pensize(1)
tim.speed("normal")

t.colormode(255)

def rbg():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    rgb=(r,g,b)
    return rgb

# angle=[0,90,270]
# distance=300
# for i in range(1,distance+1):
#     tim.color(rbg())
#     tim.forward(20)
#     tim.left(random.choice(angle))

for i in range(100):
    tim.circle(50)
    tim.pencolor(rbg())
    tim.left(15)





screen=t.Screen()
screen.exitonclick()
