from turtle import Screen, Turtle
import time
from snake import Snake # Assuming snake is defined elsewhere
from food import Food # Assuming food is defined elsewhere
from scoreboard import ScoreBoard # Assuming scoreboard is defined elsewhere

# Constants for Collision
SIMPLE_FOOD_DISTANCE = 15
BIG_FOOD_DISTANCE = 25

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food(screen) # Pass the screen object to Food
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.right,key='Right')
screen.onkey(fun=snake.left,key='Left')
game_is_on = True





def game_loop():
# while game_is_on:
    global game_is_on
    if game_is_on:
        screen.update()
        # time.sleep(0.08)
        snake.move()
        big_circle = False
            
            
            
        if food.is_big_circle_active:
            EATING_DISTANCE = BIG_FOOD_DISTANCE
        else:
            EATING_DISTANCE = SIMPLE_FOOD_DISTANCE

        # Detect collision with food
        if snake.head.distance(food) < EATING_DISTANCE:
            
        
            scoreboard.increment_score()
            scoreboard.current_score()
            snake.extend()
            
            if food.is_big_circle_active: ### here we are resetting big_circle condition to false when it was eaten
                food.simple_circle() 
                food.refresh()
                
            elif scoreboard.score % 4 == 0:
                food.big_circle() # setting big circle to True to show the big cicle
                
            else:
                food.refresh()
            

        # Detect moving past wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            ## mirror the snake
            # print((snake.head.xcor(),snake.head.ycor()))
            # snake.head.sety(-280)
            snake.mirror()
            # game_is_on = False
            # scoreboard.game_over() 


        # Detect collision with any segment in the tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                print('Inside detecting collision with itself segment')
                # game_is_on=False
                # scoreboard.game_over()
                scoreboard.reset()
                snake.reset()
                
        screen.ontimer(game_loop,80)
    else:
        return
    
game_loop()
    
screen.exitonclick()