import colorgram
import turtle
from turtle import Screen
import random

turtle.colormode(255)
tim = turtle.Turtle()


# colors = colorgram.extract('Day 18/image.jpg', 2**10)

# all_colors = []
# for i in range(len(colors)):
        
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     all_colors.append((r,g,b))

# print(all_colors)
# print(len(all_colors))
all_colors = [(229, 234, 240), (232, 242, 239), (1, 9, 29), (246, 240, 245), (121, 95, 42), (75, 33, 22), (238, 211, 73), (221, 80, 59), (229, 117, 99), (178, 139, 168), (92, 1, 21), (151, 91, 116), (9, 153, 72), (35, 89, 26), (205, 65, 92), (220, 178, 218), (2, 63, 146), (167, 129, 76), (3, 81, 31), (5, 220, 216), (80, 134, 179), (80, 113, 142), (131, 157, 179), (124, 9, 31), (117, 188, 167), (9, 216, 223), (245, 204, 5), (231, 172, 164), (137, 222, 206), (188, 190, 199), (74, 69, 45), (90, 50, 44),(124, 222, 227)]


# y = -100


# for i in range(10):
#     # tim.penup()
#     # tim.setx(-200)
#     # tim.sety(y)
#     for j in range(10):
#         tim.dot(20,random.choice(all_colors))
#         tim.penup()
#         tim.forward(50)
#     # y+=25
#     tim.setheading(90)
#     tim.forward(50)
#     tim.setheading(180)
#     tim.forward(500)
#     tim.setheading(0)

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed('fastest')

number_dots = 100
for dots_count in range(1,number_dots+1):
    
    tim.dot(20,random.choice(all_colors))
    tim.forward(50)
    if dots_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
    


screen = Screen()
screen.exitonclick()


