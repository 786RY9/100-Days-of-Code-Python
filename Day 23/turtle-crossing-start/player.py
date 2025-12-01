STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
import turtle
from turtle import Turtle
from car_manager import CarManager

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_player()
        self.go_to_start()
        
    def create_player(self):
        self.shape('turtle')
        self.setheading(90)
        self.penup()
     
    
    def have_reached_finish_line(self):
        if self.ycor()<FINISH_LINE_Y:
            return False
        else:
            return True
    def move_up(self):
        
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
            
            
