from turtle import Turtle, Screen
import turtle
from paddle import Paddle


dotted_lines = []
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = (0,0)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-50,y=300)
        self.show_scoreboard()
        
        
    def show_scoreboard(self):
        self.clear()
        self.write(f"{self.score[0]}        {self.score[1]}","center", font=("Arial",24,"bold"))
          
        for i in range(46):
            if i < 23:
                self.add_dotted_line((0,i*10))
                self.add_space_between_dotted_line((0,(i*10+5)))
            else:
                self.add_dotted_line((0,-i*15))
                self.add_space_between_dotted_line((0,(-i*10-5)))
                
            
    
    def add_dotted_line(self, position):
        global dotted_lines
        new_segment = Turtle("square")
        new_segment.speed("fastest")
        new_segment.shapesize(stretch_len=2, stretch_wid=0.4)
        new_segment.tilt(90)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        dotted_lines.append(new_segment)
        
    def add_space_between_dotted_line(self, position):
        space = Turtle('square')
        space.speed("fastest")
        space.hideturtle()
        space.fillcolor('')
        space.penup()
        space.goto(position)
        space.shapesize(stretch_len=1, stretch_wid=0.4)
    








