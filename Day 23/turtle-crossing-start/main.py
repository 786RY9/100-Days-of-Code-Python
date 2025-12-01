import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()



player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
game_loop_runs = 0

screen.update()






def game_loop():
    # loading global variables
    global game_loop_runs
    global level_passed
    global game_is_on
    global STARTING_MOVE_DISTANCE
    
    
    
    if game_is_on:
        # checking Hit of turtle with a car
        car_manager.move_cars(car_manager.speed, player=player)
        
        
        # generating car every 6th of game loop      
            # if game_loop_runs%6 == 0:
            #     car_manager.generate_car()
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car_manager.generate_car()
        
        for car in car_manager.all_cars:
            if car.distance(player)<28:
            # if abs(car.xcor() - player.xcor()) <= 47 and abs(car.ycor() - player.ycor()) <= 37:
            # if car.xcor() - 40 < player.xcor() < car.xcor() + 40 and abs(car.ycor() - player.ycor()) < 20:
                print('Hit with a car')
                game_is_on = False
                screen.update()
                scoreboard.show_game_over()
                
                # scoreboard.game_over() 
                return
        game_loop_runs+=1
       
        if player.have_reached_finish_line():
            car_manager.increase_cars_speed()
            player.go_to_start()
            scoreboard.increase_level()
            scoreboard.show_level()
            
        screen.update()
        screen.ontimer(game_loop,50)
    else:
        return
    


game_loop()
        
screen.exitonclick()
    
