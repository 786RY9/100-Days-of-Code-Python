import random
print('Welcome to rock, paper and scissors Game')
########## Add images for rock,paper,scissors and an background image from folder: pics
score = 0
c_score = 0

rps_list = ['rock','paper','scissors']

while True:
    your_choice = input("Enter your choice from {rock,paper,scissors} like 1 for rock, 2 for paper and 3 for scissors and q or any character to quit playing\n")
    computer_choice = random.randint(0,2)
    if your_choice == 'q' or int(your_choice) not in [1,2,3]:
        break
    if rps_list[int(your_choice)-1] == 'rock' and rps_list[computer_choice] == 'paper':
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print('Computer Wins!')
        
        c_score+=1
    elif rps_list[int(your_choice)-1] == 'rock' and rps_list[computer_choice] == 'scissors':
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print('You Win!')
        score+=1
    elif rps_list[int(your_choice)-1] == 'paper' and rps_list[computer_choice] == 'scissors':
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print('Computer Wins!')
        c_score+=1
    elif rps_list[int(your_choice)-1] == 'paper' and rps_list[computer_choice] == 'rock':
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print('You Win!')
        score+=1
    elif rps_list[int(your_choice)-1] == 'scissors' and rps_list[computer_choice] == 'rock':
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print('Computer Wins!')
        c_score+=1
    elif rps_list[int(your_choice)-1] == 'scissors' and rps_list[computer_choice] == 'paper':
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print('You Win!')
        score+=1
    
    else:
        print(f'Your Choice: {rps_list[int(your_choice)-1]}')
        print(f"Computer's Choice: {rps_list[computer_choice]}")
        print("It's a Tie!\n Play Again")
    print(f'Your Score: {score}')
    print(f"Computer's Score: {c_score}")
        
print('Thanks for Playing.\n  Game Ended!')
