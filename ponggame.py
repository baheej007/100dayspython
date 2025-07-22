from turtle import Turtle,Screen
import turtle
from u1u2 import move
from ball import ball
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title('Pong')
# screen.tracer(0)

t=turtle.Turtle()
u1=move((380,0))
u2=move((-380,0))
ball=ball()

screen.listen()
screen.onkey(u1.up, "Up")
screen.onkey(u1.down, "Down")
screen.onkey(u2.up, "w")
screen.onkey(u2.down, "s")


game=True
while game:
    screen.update()
    ball.move()
    if ball.ycor()>300 or ball.ycor()<-300:
        ball.bouncey()
    if ball.distance(u1)<50 and ball.xcor()>360:
        ball.bouncex()
    if ball.distance(u2)<50 and ball.xcor()<-360:
        ball.bouncex()
    if ball.xcor()>380:
        game=False
        print("LEFT WIN")
    if ball.xcor()<-380:
        game=False
        print("RIGHT WIN")






screen.exitonclick()

