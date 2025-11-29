from turtle import Turtle, Screen
import random
    

MAX_RADIUS = 4.0 
MIN_RADIUS = 0.5 
GROWTH_STEP = 0.5 
ANIMATION_SPEED = 50 
BIG_CIRCLE_DURATION = 8000 

class Food(Turtle):
    
    def __init__(self, screen): 
        super().__init__()
        self.screen = screen 
        self.current_radius = MIN_RADIUS
        self.increasing = True 
        self.is_big_circle_active = False
        self.simple_circle()
        self.refresh()
    
    
    def simple_circle(self):
        self.is_big_circle_active = False
        # self.screen.ontimer(lambda: None, 1) # This is a trick to cancel pending timers (though not guaranteed)
        
        self.shape('circle')
        self.shapesize(stretch_wid=MIN_RADIUS, stretch_len=MIN_RADIUS)
        self.color('blue')
        self.penup()
        self.speed('fastest')
        # self.refresh()
        
    def reset_and_move(self):
        if self.is_big_circle_active: ### still big_circle was not eaten and time was over then set condition to false for big_circle
            print("Timer expired: Big Circle was NOT eaten. Resetting and moving.")
            self.simple_circle() 
            self.refresh()      
        else:
            # snake ate the big circle early and the collision logic already 
            # called simple_circle() and refresh(). We do nothing here.
            print("Timer expired: Big Circle was eaten early. Ignoring refresh.")
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def animate_circle(self):
        if not self.is_big_circle_active:
            # Stop animating if the 8-second period is over
            return

        self.shapesize(stretch_len=self.current_radius, stretch_wid=self.current_radius)

        if self.increasing:
            self.current_radius += GROWTH_STEP
        else:
            self.current_radius -= GROWTH_STEP

        if self.current_radius >= MAX_RADIUS:
            self.increasing = False
        elif self.current_radius <= MIN_RADIUS + GROWTH_STEP: 
            self.increasing = True
            
        # Schedule the next animation frame
        self.screen.ontimer(self.animate_circle, ANIMATION_SPEED)

    def big_circle(self):
        # Set state to big circle
        self.is_big_circle_active = True
        self.current_radius = MAX_RADIUS # Start big
        self.color('red')
        
        # Move to a new random position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        
        # starting the big circle size animation
        self.animate_circle()
        
        # calling simple_circle after 8 seconds
        self.screen.ontimer(self.reset_and_move, BIG_CIRCLE_DURATION)
        # self.refresh()