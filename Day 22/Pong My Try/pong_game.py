from turtle import Turtle, Screen
import turtle
from paddle import Paddle
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=700,width=900)
screen.listen()
screen.bgcolor('black')


scoreboard = ScoreBoard()
scoreboard.setx(-30)
scoreboard.sety(330)

paddle1 = Paddle(5)
paddle1.setx(-435)

paddle2 = Paddle(5)
paddle2.setx(435)







screen.exitonclick()
























