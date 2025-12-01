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
            new_segment = Turtle('square')
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
    
        current_x = self.head.xcor()
        current_y = self.head.ycor()
        
        # Warping across the horizontal boundaries
        if current_x > 290 and self.head.heading() == RIGHT:
            print("snake went through right wall")
            self.head.setx(-290) 
            
        elif current_x < -290 and self.head.heading() == LEFT:
            print("snake went through left wall")
            
            self.head.setx(290)
            
        if current_y > 290 and self.head.heading() == UP:
            print("snake went through up wall")
            self.head.sety(-290)
            
        elif current_y < -290 and self.head.heading() == DOWN:
            print("snake went through down wall")
            self.head.sety(290)
        
    def move(self):
        
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        print('inside up function')
        cur_heading = self.head.heading()
        if cur_heading == DOWN or cur_heading == UP:
            
            return
        else:
            self.head.setheading(UP)
    def down(self):
        print('inside down function')
        cur_heading = self.head.heading()
        if cur_heading == UP or cur_heading == DOWN:
            return
        else: 
            self.head.setheading(DOWN)
    def right(self):
        print('inside right function')
        cur_heading = self.head.heading()
        if cur_heading == LEFT or cur_heading == RIGHT:
            return
        elif cur_heading == UP or cur_heading == DOWN:
            self.move()
            self.head.setheading(RIGHT)
        else:
            self.head.setheading(RIGHT)
    def left(self):
        print('inside left function')
        cur_heading = self.head.heading()
        if cur_heading == RIGHT or cur_heading == LEFT:
            return
        elif cur_heading == UP or cur_heading == DOWN:
            self.move()
            self.head.setheading(LEFT)
        else:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]