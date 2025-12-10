BACKGROUND_COLOR = "#B1DDC6"
import tkinter
from tkinter import *
import pandas as pd
import random
import csv

try:
    data = pd.read_csv("Day 31/flash-card-project-start/data/words_to_learn_csv.csv")
except FileNotFoundError:
    data = pd.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
    df = pd.DataFrame(data)
    df.to_csv("Day 31/flash-card-project-start/data/words_to_learn_csv.csv",index=False)
        


learnt = []
current_word = {}
words_to_learn = data.to_dict(orient='records')
# print('words to learn: ', words_to_learn)
# with open('words_to_learn_csv.csv',mode='w') as file:
#     file.write(words_to_learn)


def knew_it():
    if current_word in words_to_learn:
        words_to_learn.remove(current_word)
        
    data = pd.DataFrame(words_to_learn)
    data.to_csv("Day 31/flash-card-project-start/data/words_to_learn_csv.csv", index=False)
    next_card()

def next_card():
    print('next card functin called')
    global flip_timer,current_word, words_to_learn
    
    # print(words_to_learn)
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    french_word = current_card['French']
    english_word = current_card['English']
    current_word = current_card
    canvas.itemconfig(front_image,image=front_image_path)
    canvas.itemconfig(card_title,text="French",fill='black')
    canvas.itemconfig(card_word,text=french_word,fill='black')
    flip_timer = window.after(3000,flip_card)
    
def flip_card():
    canvas.itemconfig(front_image,image=image)
    canvas.itemconfig(card_title,text="English",font=("Ariel",40,"italic",),fill='white')
    canvas.itemconfig(card_word,text=current_word['English'],font=("Ariel",40,"italic"),fill='white')
    
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

image_path = "Day 31/flash-card-project-start/images/card_back.png"
image = PhotoImage(file=image_path)
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
# background_image = canvas.create_image(400,263,image=image)

front_image_path = PhotoImage(file="Day 31/flash-card-project-start/images/card_front.png")
front_image = canvas.create_image(400,263,image=front_image_path)

card_title = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))

card_word = canvas.create_text(400,263,text="trouve",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_btn_img = PhotoImage(file="Day 31/flash-card-project-start/images/wrong.png")
wrong_btn = Button(image=wrong_btn_img,highlightthickness=0,command=next_card)
wrong_btn.grid(column=0,row=1)

right_btn_img = PhotoImage(file="Day 31/flash-card-project-start/images/right.png")
right_btn = Button(image=right_btn_img,command=knew_it,highlightthickness=0)
right_btn.grid(column=1,row=1)

flip_timer = window.after(3000,flip_card)
next_card()


    
    
# def next_card():
#   data_dict = data.to_dict()
#     print(data_dict)
#     random_index = random.randint(0,len(data_dict['French']))
#     if random_index not in learnt:
#         french_word = data_dict['French'][random_index]
#         english_word = data_dict['English'][random_index]
#         print(french_word,english_word)
#         canvas.itemconfig(french,text=french_word)
#         canvas.itemconfig(english,text=english_word)
#         learnt.append(random_index)
        
def new_card():
    pass

window.mainloop()
