from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color('white')  
        self.sety(270)
        self.current_score()  
        self.penup()
    def increment_score(self):
        self.score += 1
    def current_score(self):
        self.clear()
        self.write(f'Score: {self.score}', False, align='center',font=('Arial',18,'normal'))
        # return self.score
