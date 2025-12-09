import pandas as pd

df = pd.read_csv("Day 30/NATO-alphabet-start/nato_phonetic_alphabet.csv")


phonetics_dict = {row.letter:row.code for (index,row) in df.iterrows()}

def generate_phonetic():
    user_input = input("Enter the word: ").upper()

    try:
        code_words = [phonetics_dict[char] for char in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
            
        print(code_words)


generate_phonetic()









