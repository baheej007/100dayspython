import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US STATE GAME")
screen.bgpic("blank_states_img.gif")

# def click_coord(x,y):                  "use to find coordinates where we click on the screen"
#     print(x,y)
#
# turtle.onscreenclick(click_coord)
# turtle.mainloop()
states=pd.read_csv("50_states.csv")

l=[]
play=True
while play:
    inp=(screen.textinput("ENTER A STATE: ","ENTER: ")).title()
    for i in states.state:
        if inp==i:
            l.append(i)
            print(l)
            if len(list(set(l)))==2:
                play = False
                screen.bgpic("y.gif")

            else:
                turtle.penup()
                turtle.hideturtle()
                forx = states[states.state == inp]
                x=int(forx.x)
                fory = states[states.state == inp]
                y=int(fory.y)
                turtle.goto(x-3,y)
                turtle.write(inp)
            play=True
        else:

            Play=True












screen.exitonclick()

