import random
import hangman_art
import hangman_words
lives = 6
print('You have 6 lives to correctly guess the word.')
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""

for pos in range(len(chosen_word)):
    placeholder+='_ '

print(hangman_art.logo)
print("Word to guess: ", placeholder)
print()
correct_letters = []

game_over = False
i = -1
already_guessed = set()
while not game_over:
    print('*'*20+f'{lives}/6 LIVES LEFT'+'*'*30)
    user_guess = input('Guess a letter: ').lower()
    
    if user_guess in already_guessed:
        print(f'You have already guessed {user_guess}')
    else:
        already_guessed.add(user_guess)
        display = ''
        if user_guess not in chosen_word and abs(i) < len(hangman_art.stages):
            
            i-=1
            lives-=1
            print(f"You guessed {user_guess} that's not in the word.")
            print('You lose a life.')
            

        for letter in chosen_word:
            if letter == user_guess:
                display+=letter
                correct_letters.append(letter)
                
            elif letter in correct_letters:
                display+=letter
            else:
                
                display+='_'
        if lives<=0:
            print('You Lose')
            print(f'Word was {chosen_word}')
            break     
                
        print(display)
        print(hangman_art.stages[i])
        if '_' not in display:
            game_over=True
            print('You win.')
        



# for i in range(len(chosen_word)):
#     correct_letters+=['_']
# game_over = False
# while not game_over:
#     user_guess = input('Guess a letter: ').lower()
#     i = 0       
#     for letter in chosen_word:
#         if letter == user_guess and user_guess!=correct_letters[i]:
#             correct_letters[i]=letter
#         i+=1
#     print(''.join(correct_letters))
#     if '_' not in correct_letters:
#         print('Game Over')
#         game_over=True
            

# print(''.join(correct_letters))


















