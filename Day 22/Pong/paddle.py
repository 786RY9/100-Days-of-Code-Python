from turtle import Turtle, Screen
import turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
        
    def create_paddle(self,position):
        self.color('white')
        self.tilt(90)
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)

    



