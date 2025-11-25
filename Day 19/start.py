import turtle
from turtle import Screen

# add functionality to skip drawing

tim = turtle.Turtle()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
    
def turn_left():
    tim.setheading(tim.heading()+10)
    
def turn_right():
    tim.setheading(tim.heading()-10)

def reset_turtle():
    turtle.resetscreen()
def skip_drawing():
    tim.penup()
def start_drawing():
    tim.pendown()

screen = Screen()
screen.listen()

screen.onkey(key='c', fun=reset_turtle)
screen.onkey(fun=move_forward,key='w')
screen.onkey(key='space',fun=skip_drawing)
screen.onkey(key='r',fun=start_drawing)

screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)

screen.exitonclick()







