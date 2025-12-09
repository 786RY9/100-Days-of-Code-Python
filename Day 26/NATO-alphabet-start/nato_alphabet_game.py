import pandas as pd


# {new_key:new_value for (index,value) in df.iterrows()}

# Todo1: create dictionary from csv as below: {"A":"Alfa","B":"bravo"...}

df = pd.read_csv("Day 26/nato_phonetic_alphabet.csv")

# print(df)

phonetics_dict = {row.letter:row.code for (index,row) in df.iterrows()}

# print(phonetics_dict)

# Todo2: create a list of phonetic code words from a word that the user inputs.

user_input = input("Enter the word: ").upper()

code_words = []
for char in user_input:
    code_words.append(phonetics_dict[char])
    
print(code_words)












