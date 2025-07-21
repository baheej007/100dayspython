from turtle import Turtle,Screen
STARTPOS=[(0,0),(-20,0),(-40,0)]
c=20
u,d,r,l=90,270,0,180
class snakec:
    def __init__(self):
        self.seg=[]
        self.createsnake()

    def createsnake(self):
        for position in STARTPOS:
            self.adds(position)
    def adds(self,position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.seg.append(new)
    def extend(self):
        self.adds(self.seg[-1].position())

    def move(self):
        for segn in range(len(self.seg)-1,0,-1):
                newx=self.seg[segn-1].xcor()
                newy=self.seg[segn-1].ycor()
                self.seg[segn].goto(newx,newy)
        self.seg[0].forward(c)


    def up(self):
       if self.seg[0].heading()!=d:
        self.seg[0].setheading(90)
    def down(self):
       if self.seg[0].heading()!= u:
        self.seg[0].setheading(270)
    def right(self):
       if self.seg[0].heading()!= l:
        self.seg[0].setheading(0)
    def left(self):
        if self.seg[0].heading()!=r:
            self.seg[0].setheading(180)