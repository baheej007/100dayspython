import turtle
from turtle import Screen,Turtle
rectangle = ((0, 0), (1, 1000), (100, 50), (0, 50))

# Register it as a new shape

turtle.register_shape("rectangle", rectangle)


t=Turtle()
t.shape("rectangle")






screen=Screen()
screen.exitonclick()