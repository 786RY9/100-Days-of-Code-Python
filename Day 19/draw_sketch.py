import turtle
from turtle import Screen

# add functionality to skip drawing

tim = turtle.Turtle()
screen = Screen()
screen.listen()

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
def choose_color():
    tim.color(screen.textinput(title='Color for skecthing',prompt='Enter color you want to use for sketching: '))
    screen.listen()



screen.onkey(key='c', fun=reset_turtle)
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='space',fun=skip_drawing)
screen.onkey(key='i',fun=choose_color)
screen.onkey(key='r',fun=start_drawing)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)

screen.exitonclick()







