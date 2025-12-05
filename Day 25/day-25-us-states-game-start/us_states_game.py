import pandas as pd
import turtle


screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(650,650)
states_data = pd.read_csv("Day 25/day-25-us-states-game-start/50_states.csv")

# print(states_positions.head())

image ="Day 25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# get position of mouse click(x,y) coordinates
# def get_mouse_click_coor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_coor)

# input_turtle = Turtle()
# input_turtle.hideturtle()
# input_turtle.penup()
# input_turtle.goto(x=-620,y=620)

correct_guess = []

while len(correct_guess) < 50:
    # turtle.penup()
    # turtle.setx(-620)
    # turtle.sety(620)
    # screen.goto(x=-620,y=620)
    user_answer = screen.textinput(title=f"{len(correct_guess)}/50 Guess the State",prompt="What's another state's name?").title()
    
    # print(user_answer)
    states_names = list(states_data["state"])
    # print(list(states_names))
    if user_answer in states_names:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = states_data[states_data["state"] == user_answer]
        correct_guess.append(user_answer)
        x_cor = list(data['x'])[0]
        y_cor = list(data['y'])[0]
        
        print(x_cor,y_cor)
        t.goto(x=x_cor,y=y_cor)
        t.write(f"{user_answer}")








