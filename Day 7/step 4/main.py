import random

word_list = ['aardvark','baboon','camel']

lives = 6
print('You have 6 lives to correctly guess the word.')
chosen_word = random.choice(word_list)

placeholder = ""

for pos in range(len(chosen_word)):
    placeholder+='_ '

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
print(placeholder)
correct_letters = []

game_over = False
i = -1
while not game_over:
    user_guess = input('Guess a letter: ').lower()
    
    display = ''
    if user_guess not in chosen_word and abs(i) < len(stages):
        
        i-=1
        lives-=1
        

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
        break     
            
    print(display)
    print(stages[i])
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


















