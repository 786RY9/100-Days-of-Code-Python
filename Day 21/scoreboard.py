from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial',16,'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color('white')  
        self.goto(x=0,y=270)
        self.current_score()  
        self.penup()
    def increment_score(self):
        self.score += 1
    def current_score(self):
        self.clear()
        self.write(f'Score: {self.score}', False, align=ALIGNMENT,font=FONT)
        # return self.score

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"Game Over!",font=FONT)