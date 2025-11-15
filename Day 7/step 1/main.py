
import random

word_list = ['aardvark','baboon','camel']

word = random.choice(word_list)

user_guess = input('Guess a letter: ').lower()

if user_guess in word:
    print('Right')
else:
    print('Wrong')



















