from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial',16,'normal')

class ScoreBoard(Turtle):
    
    def read_highscore(self):
        with open("Day 21/data.txt") as file:
            highscore = int(file.read())
        return highscore
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.highscore = self.read_highscore()
        self.score = 0
        self.color('white')  
        self.goto(x=0,y=270)
        self.current_score()  
        self.penup()
    def increment_score(self):
        self.score += 1
    def current_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', False, align=ALIGNMENT,font=FONT)
        # return self.score

    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write(f"Game Over!",font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore(self.highscore)
            
        self.score = 0
        self.current_score()
    
    def update_highscore(self, highscore):
        with open("Day 21/data.txt", mode="w") as file:
            file.write(str(highscore))
        print(f'inside update_highscore function: {self.highscore}')