from art import logo
import random

def generate_random_number():
    return random.randint(1,100)

def give_suggestion(guess,actual_number):
    if guess > actual_number:
        return 'Too High!'
    elif guess < actual_number:
        return 'Too Low!'
    else:
        return 'guessed'
    

def play_game():
    # Logo
    print(logo)
    actual_number = generate_random_number()
    easy_or_hard = input("""Welcome to the Number Guessing Game!\n
    I'm thinking of a number between 1 and 100.\n
    Choose a difficulty. Type 'easy' or 'hard': """).lower()
    lives = 0
    if easy_or_hard in ['easy','hard']:
        if easy_or_hard == "easy":
            lives = 10
        elif easy_or_hard=="hard":
            lives = 5
        suggestion = ''
        while suggestion!='guessed' and lives>0:
            print(f"You have {lives} attempts remaining to guess the number.")
            user_guess = int(input('Make a guess: '))
            suggestion = give_suggestion(user_guess,actual_number=actual_number)
            if suggestion!='guessed':
                print(suggestion)
            lives-=1
        print(f"Actual Number was {actual_number}")
        if lives<=0 and suggestion!='guessed':
            print("You have no attempts left, and weren't able to guess the  number.")
        else:
            print("You Guessed It!")
    else:
        print('Please choose between "easy",or "hard".')
keep_playing=True
while keep_playing:
    play_game()
    
    