import turtle
from turtle import Turtle,Screen
import random

colors = ['red','orange','green','yellow','blue','purple']
screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
turtles_list= []
user_guess = screen.textinput(title='Make a guess who will win!', prompt='Enter your guess by entering the color of turtle: ')

for i,color in enumerate(colors):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.goto(x=-230,y=-110+(i*40))
    turtles_list.append(t)
    

if user_guess:
    is_race_on = True

while is_race_on:
    
    
    
    for turtle in turtles_list:
        if turtle.xcor() >230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            break
        turtle.forward(random.randint(0,10))

if winning_turtle == user_guess.lower():
    print(f"You've won. {winning_turtle} turtle has won the race!")
else:
    print(f"You've Lost. {winning_turtle} turtle has won the race!")



screen.exitonclick()












