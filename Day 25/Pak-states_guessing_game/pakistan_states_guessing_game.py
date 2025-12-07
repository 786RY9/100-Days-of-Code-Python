import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(600,600)
image = "Day 25/Pak-states_guessing_game/pak_blank_states.gif"
screen.addshape(image)
turtle.shape(image)


# pakistan_states = ['Balochistan', "Sindh","Punjab", "Kpk","Azad Jammu Kashmir","Gilgit Baltistan"]

# def generate_coordinates(x,y):
#     print((x,y))
    
# screen.onscreenclick(fun=generate_coordinates)


# states_cords = [
#     (-129.0, -73.0),
# (-41.0, -160.0),
# (66.0, -0.0),
# (24.0, 107.0),
# (175.0, 123.0),
# (139.0, 197.0),
# ]


# states_dict = {
#     "Province": pakistan_states,
#     "x": [cord[0] for cord in states_cords],
#     "y": [cord[1] for cord in states_cords]
# }


# pakistan_df = pd.DataFrame(states_dict)
# pakistan_df.to_csv('Pakistan_states_with_cords.csv')

# turtle.mainloop()

correct_guess = []
pak_provinces = pd.read_csv("Day 25/Pak-states_guessing_game/Pakistan_states_with_cords.csv")
pak_provinces_names = pak_provinces["Province"].to_list()
# print(pak_provinces)
missing_states=[]
while len(correct_guess) < 6:
    
    user_answer = screen.textinput(title=f"{len(correct_guess)}/6", prompt="Guess another state.").title()
    if user_answer == 'Exit':
        missing_states = [province for province in pak_provinces_names if province not in correct_guess]
        print(missing_states)
        print(correct_guess)
        to_learn_provinces = pd.DataFrame(missing_states)
        to_learn_provinces.to_csv("To_learn_Pakistan_Provinces.csv")
        break
    
    if user_answer in pak_provinces_names:
        correct_guess.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = pak_provinces[pak_provinces['Province'] == user_answer]
        t.goto(row['x'].item(),row['y'].item())
        t.write(user_answer)
























