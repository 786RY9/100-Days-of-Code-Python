
import random
from art import logo

def deal_card(cards):
    return random.choice(cards)

def calculate_score(cards_list):
    cards_sum = sum(cards_list)
    if len(cards_list) == 2 and sum(cards_list) == 21:
        return 0
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)

def compare(u_score,c_score):
    if c_score==u_score:
        return 'Draw 🙃'
    elif c_score==0:
        return 'Lose, opponent has Blackjack 😱'
    elif u_score == 0:
        return 'Win with a Blackjack 😎'
    elif u_score>21:
        return  'You went over. You lose 😭'
    elif c_score>21:
        return 'Opponent went over. You win 😁'
    elif u_score>c_score:
        return 'You win 😃'
    else:
        return 'You lose 😤'

def play_game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    computer_score= -1
    user_score = -1
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_another_card == 'y':
                user_cards.append(deal_card(cards))
                user_score = calculate_score(user_cards)
                if computer_score == 0 or user_score == 0 or user_score > 21:
                    is_game_over = True
            elif draw_another_card == 'n':
                is_game_over = True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play_game()
play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_or_not=='y':
    print('\n'*25)
    play_game()
print('Bye!')










