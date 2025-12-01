from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
cars_list = []


def generate_car():
    car = Turtle('square')
    car.color('red')
    car.shapesize(stretch_len=4, stretch_wid=2)
    car.penup()
    car.setheading(180)
    y_pos = random.randint(-230,230)
    car.goto(x=230,y=y_pos)
    cars_list.append(car)
    
def move_cars():
    
    for car in cars_list:
        car.forward(10)
        
    screen.update()
    screen.ontimer(move_cars,100)


game_is_on = True
game_loop_runs = 0
def game():
    global game_loop_runs
    if game_loop_runs%6 == 0:
        generate_car()
    game_loop_runs+=1
    screen.update()
    
    # car.forward(10)
    
    
    screen.ontimer(game,100)

game()
# screen.ontimer(move_cars,100)
move_cars()





screen.exitonclick()

















