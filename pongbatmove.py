from turtle import Screen
screen=Screen()
class move:
    def __init__(self,bat,upb,downb):
          screen.listen()
    def up(self,bat):
        super().__init__()
            bat.forward(40)

        screen.onkey(up, "Up")

    def down():
            bat.backward(40)

        screen.onkey(down, "Down")