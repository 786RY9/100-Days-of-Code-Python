import turtle
from turtle import Turtle,Screen

##### 

tim = Turtle(shape='turtle')
screen = Screen()
screen.listen()
screen.setup(width=800, height=600)

user_color = screen.textinput(title='Turtle color', prompt='What color turtle you want to have? ')
if user_color:
    tim.color(user_color)
tim.shapesize(2)
tim.penup()
tim.goto(x=-380,y=-270)
# tim.forward(100)
screen.listen()

is_hit = False

while not is_hit:
    
    
    
    tim.forward(1)

    









screen.exitonclick()




























