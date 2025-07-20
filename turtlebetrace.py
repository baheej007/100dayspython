from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=1000,height=600)
u=screen.textinput(title="select a color",prompt="your color")

l1=Turtle()
l1.shape("circle")
l1.pensize(10)
l1.penup()
l1.goto(290,-350)
l1.pendown()
l1.goto(290,350)


t1=Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-470,100)

t2=Turtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(-470,-100)

t3=Turtle()
t3.shape("turtle")
t3.color("green")
t3.penup()
t3.goto(-470,35)

t4=Turtle()
t4.shape("turtle")
t4.color("yellow")
t4.penup()
t4.goto(-470,-35)


rs=0
bs=0
gs=0
ys=0
def rm():
    global rs
    k=random.randint(1, 7)
    t1.forward(k)
    rs+=k
    if rs<770:
        bm()
    else:
         t1.circle(5)
         if u=="red":
             print("YOU WIN")
         else:
             print("YOU LOSE")
def bm():
    global bs
    j=random.randint(1, 7)
    t2.forward(j)
    bs+=j
    if bs<770:
        gm()
    else:
        t2.circle(5)
        if u == "blue":
            print("YOU WIN")
        else:
            print("YOU LOSE")
def gm():
    global gs
    k=random.randint(1, 7)
    t3.forward(k)
    gs+=k
    if gs<770:
        ym()
    else:
        t3.circle(5)
        if u == "green":
            print("YOU WIN")
        else:
            print("YOU LOSE")
def ym():
    global ys
    j=random.randint(1,7)
    t4.forward(j)
    ys+=j
    if ys<770:
        rm()
    else:
        t4.circle(5)
        if u == "yellow":
            print("YOU WIN")
        else:
            print("YOU LOSE")



bm()


screen.exitonclick()