FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.show_level()
    
    def show_level(self):
        self.clear()
        self.goto(x=-260,y=260)
        self.write(f"Level: {self.level}", font=FONT)
    def increase_level(self):
        self.level+=1
    def show_game_over(self):
        self.goto(x=-80,y=0)
        self.write(f"Game Over",font=FONT)
