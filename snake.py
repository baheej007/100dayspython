from turtle import Screen
from snakescore import Scores
from snakeclass import snakec
from snakefood import food
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("SNAKE AND APPLE")
screen.tracer(0)






snake=snakec()
score=Scores()
food=food()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

move=True
while move:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.seg[0].xcor()>280 or snake.seg[0].xcor()<-280 or snake.seg[0].ycor()>280 or snake.seg[0].ycor()<-280:
        score.gameover()
        move=False

    for i in snake.seg[1:]:

        if snake.seg[0].distance(i)<10:
                score.gameover()
                move = False


    if snake.seg[0].distance(food)<15:
        score.add()
        food.ref()
        snake.extend()



screen.exitonclick()









































screen.exitonclick()