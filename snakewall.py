from turtle import Turtle,Screen
STARTPOS=[(300,-300),(300,300),(-300,300),(-300,-300)]
size=[(1,300),(300,1),(1,300),(300,1)]
rectangle = ((0, 0), (100, 0), (100, 50), (0, 50))

turtle.register_shape("rectangle", rectangle)
sc=0
class wallc:
    def __init__(self):
        self.seg=[]
        self.createwall()

    def createwall(self):
        for position in STARTPOS:
            new = Turtle()
            new.color("white")
            new.shapesize(size[sc][0],size[sc][1])
            new.penup()
            new.goto(position)
            self.seg.append(new)
