from turtle import *
t=Turtle()
t.shape("arrow")
t.co
# def r():
#   timmy.forward(100)
#   timmy.right(90)
# r()
# r()
# r()
# r()
#
# for i in range(50):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#
# def draw(i,s):
#     for _ in range(s):
#         t.forward(50)
#         t.right(i)
#
#
# angle=[]
# u=14
# for i in range(3,int(u)+3):
#     angle.append(int(360/i))
# s=2
# for i in angle:
#     s+=1
#     print(i,s)
#     draw(i,s)
#     t.right(90)
#     t.right(90)
#     t.right(90)
#     t.right(90)


t.pensize(10)
t.speed("fastest")

import random
angle=[0,90,270]
color=["red","blue","green","yellow"]
distance=300
for i in range(1,distance+1):
    t.color(random.choice(color))
    t.forward(20)
    t.left(random.choice(angle))































screen=Screen()
screen.exitonclick()
