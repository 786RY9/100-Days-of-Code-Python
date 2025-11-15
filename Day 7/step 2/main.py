
import random

word_list = ['aardvark','baboon','camel']

chosen_word = random.choice(word_list)
placeholder = ""
for pos in range(len(chosen_word)):
    placeholder+='_ '
print(placeholder)
user_guess = input('Guess a letter: ').lower()
display = ''
for letter in chosen_word:
    if letter == user_guess:
        display+=f'{letter}'
    
    else:
        display+='_ '
print(display)


















