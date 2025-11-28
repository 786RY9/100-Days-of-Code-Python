from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.right,key='Right')
screen.onkey(fun=snake.left,key='Left')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
        
    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increment_score()
        scoreboard.current_score()
        # print(scoreboard.score)
        
        food.refresh()


screen.exitonclick()


