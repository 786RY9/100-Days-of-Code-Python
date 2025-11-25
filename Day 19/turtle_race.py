import turtle
from turtle import Turtle,Screen


colors = ['red','orange','green','yellow','blue','purple']
screen = Screen()

screen.setup(width=500,height=400)
turtles= []

for i,color in enumerate(colors):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.goto(x=-230,y=-100+(i*100))
    turtles.append(t)
    
    
    



screen.exitonclick()












