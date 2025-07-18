from turtle import Turtle,Screen
def u():
   for i in range(3):
           timmy.forward(400)
           timmy.left(90)
           timmy.forward(40)
           timmy.left(90)
           timmy.forward(800)
           timmy.right(90)
           timmy.forward(40)
           timmy.right(90)
           timmy.forward(400)
def d():
    timmy.right(90)
    timmy.right(90)
    u()


def s1():
    u()
    d()
    u()
    d()
def s2():
    timmy.left(90)
    s1()


timmy=Turtle()
timmy.shape("turtle")
timmy.color("coral")
s1()
s2()
myscreen=Screen()
print(myscreen.canvheight)
myscreen.exitonclick()






























