from turtle import Turtle

STARTING_POSITIONS = [ (-20, 0), (-40, 0)]
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
        i = 0
        if i ==0:
            new_segment = Turtle('turtle')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto((0,0))
            self.segments.append(new_segment)
            i+=1
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def mirror(self):
        print('Inside mirror function')
        # if self.head.heading() == UP:
        #     # print(self.head.heading())
        #     self.head.sety(-280)
        # elif self.head.heading() == DOWN :
        #     self.head.sety(280)
        # elif self.head.heading() == LEFT:
        
        #     self.head.setx(290)
        # elif self.head.heading() == RIGHT:
        #     self.head.setx(-290)
    
        current_x = self.head.xcor()
        current_y = self.head.ycor()
        
        # Warping across the horizontal boundaries
        if current_x > 280 and self.head.heading() == RIGHT:
            # Snake went off the right edge, warp to the left edge
            # We set it to -280 (or -270) to place it just inside the boundary
            self.head.setx(-280) 
            
        elif current_x < -280 and self.head.heading() == LEFT:
            # Snake went off the left edge, warp to the right edge
            self.head.setx(280)
            
        # Warping across the vertical boundaries
        if current_y > 280 and self.head.heading() == UP:
            # Snake went off the top edge, warp to the bottom edge
            self.head.sety(-280)
            
        elif current_y < -280 and self.head.heading() == DOWN:
            # Snake went off the bottom edge, warp to the top edge
            self.head.sety(280)
        
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

