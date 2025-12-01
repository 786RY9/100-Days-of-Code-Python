COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random



class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        global STARTING_MOVE_DISTANCE
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        
        
        
    def generate_car(self):
        self.hideturtle()
        new_car = Turtle('square')
        new_car.penup()
        color_s = random.choice(COLORS)
        new_car.color(color_s)
        new_car.shapesize(stretch_len=4, stretch_wid=2)
        new_car.setheading(180)
        y_pos = random.randint(-230,230)
        new_car.goto(x=280,y=y_pos)
        self.all_cars.append(new_car)
        return new_car
    
    def increase_cars_speed(self):
        global MOVE_INCREMENT
        global STARTING_MOVE_DISTANCE
        self.speed += MOVE_INCREMENT
        print(f'Increased cars speed by: {MOVE_INCREMENT}')
        print(f"{self.speed}")
    
        # screen.ontimer(self.move_cars,100)
            
    
    def move_cars(self,speed, player):
        print('inside move_cars function')
        print(f'speed: {speed}')
        for car in self.all_cars:
            car.forward(speed)  