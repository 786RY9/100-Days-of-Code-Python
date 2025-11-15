import random

word_list = ['aardvark','baboon','camel']

chosen_word = random.choice(word_list)

placeholder = ""

for pos in range(len(chosen_word)):
    placeholder+='_ '
    
print(placeholder)

length = len(chosen_word)



correct_letters = []

game_over = False
while not game_over:
    user_guess = input('Guess a letter: ').lower()
    display = ''
    for letter in chosen_word:
        if letter == user_guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
    print(display)
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


















