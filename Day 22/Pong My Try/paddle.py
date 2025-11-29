from turtle import Turtle, Screen
import turtle




class Paddle(Turtle):
    
    def __init__(self,stretch_len):
        super().__init__()
        self.create_paddle(stretch_len)
        
    def create_paddle(self, stretch_len):
        # self.speed("fastest")
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=stretch_len, stretch_wid=0.4)
        self.tilt(90)
        


