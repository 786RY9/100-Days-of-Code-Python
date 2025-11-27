from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180



class Snake:
    
    def __init__(self):
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

        
    
    

    def move(self):
        
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # print('inside up function')
        cur_heading = self.head.heading()
        if cur_heading == DOWN:
            return
        else:
            self.head.setheading(UP)
    def down(self):
        cur_heading = self.head.heading()
        if cur_heading == UP:
            return
        else: 
            self.head.setheading(DOWN)
    def right(self):
        cur_heading = self.head.heading()
        if cur_heading == LEFT:
            return
        else:
            self.head.setheading(RIGHT)
    def left(self):
        cur_heading = self.head.heading()
        if cur_heading == RIGHT:
            return
        else:
            self.head.setheading(LEFT)

