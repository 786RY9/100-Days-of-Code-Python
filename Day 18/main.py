import turtle as t 
from turtle import Turtle, Screen
import random


t.colormode(255)
tim = Turtle()

tim.shape('classic')
# tim.color('green','red')

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(0,100,10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

shapes = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8, 'nonagon':9,'decagon': 10}

colors = ['cyan', 'brown', 'black','sea green', 'dark green', 'deep sky blue', 'cornsilk2', 'burlywood1']

def draw_shape(shape,sides,color_t):
    
    rotation_angle = 360/sides
    
    tim.color(random.choice(colors))
    for i in range(sides):
        tim.forward(100)
        tim.right(rotation_angle)
    
def change_direction(direction):
    if direction == 'east' and tim.heading() == 0:
        return
    elif direction == 'east' and tim.heading() == 270:
        tim.left(90)
    elif direction == 'east' and tim.heading() == 180:
        tim.right(180)
    elif direction == 'east' and tim.heading() == 90:
        tim.right(90)
    
    elif direction == 'west' and tim.heading() == 0:
        tim.right(180)
    elif direction == 'west' and tim.heading() == 270:
        tim.right(90)
    elif direction == 'west' and tim.heading() == 180:
        return
    elif direction == 'west' and tim.heading() == 90:
        tim.left(90)
    
    elif direction == 'north' and tim.heading() == 0:
        tim.left(90)
    elif direction == 'north' and tim.heading() == 270:
        tim.right(180)
    elif direction == 'north' and tim.heading() == 180:
        tim.right(90)
    elif direction == 'north' and tim.heading() == 90:
        return

    elif direction == 'south' and tim.heading() == 0:
        tim.right(90)
    elif direction == 'south' and tim.heading() == 270:
        return
    elif direction == 'south' and tim.heading() == 180:
        tim.left(90)
    elif direction == 'south' and tim.heading() == 90:
        tim.right(180)
    
    
    
        

def do_a_random_walk():
    tim.speed(0)
    tim.hideturtle()
    tim.pensize(10)
    directions = ['north','south','east','west']
    # it is initially facing towards east -> to the left
    for i in range(200):
        direction = random.choice(directions)
        print(f'Turned towards direction of: {direction}')
        color_t = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.color(color_t)
        change_direction(direction)
        tim.forward(30)
    
# i = 0    
# for shape, sides in shapes.items():
#     draw_shape(shape,sides,colors[i])
#     i+=1


# do_a_random_walk()
def draw_spirograph(gap):
    
    tim.speed('fastest')
    for _ in range(int(360/gap)):
        tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        tim.setheading(tim.heading()+gap)
        tim.circle(100)
        
        
draw_spirograph(5)






screen = Screen()
screen.exitonclick()















