from turtle import Turtle, Screen
import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong Game')
screen.tracer(0)


right_paddle = Paddle((350,0))

left_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = ScoreBoard()


     

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(ball.move_speed)
def game_loop():
    screen.update()
    ball.move_ball()
    
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
        
    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    
    # Detect when left or right paddle misses
    # right player misses
    if scoreboard.lscore>=50 or scoreboard.rscore>=50:
        return
    if ball.xcor() > 380:
         ball.reset()
         scoreboard.inc_l_point()
         
         
    # left player misses
    if ball.xcor() <- 380:
        ball.reset()
        scoreboard.inc_r_point()

    screen.ontimer(game_loop,int(ball.move_speed*1000))

game_loop()

screen.exitonclick()

