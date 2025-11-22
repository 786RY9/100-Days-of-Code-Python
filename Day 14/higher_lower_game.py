import pandas as pd
import csv
import random
from art import logo,vs

# We need list of celebrities or things with number of followers they have, it could from a csv file. At first choose 2 from that csv at random 
def load_data(path):

    narrators_dict = {}
    with open(path,newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        header = next(csv_reader) # skipping header
        for row in csv_reader:
            # print(row[0] + "      " + row[1])
            narrators_dict[row[0]] = row[1]
        # csv_reader has names and values
    return narrators_dict
# print(narrators_dict)

def compare(first_person_narrations,second_person_narrations,user_answer):
    highest_hadith_narrator = ''
    if first_person_narrations > second_person_narrations:
        highest_hadith_narrator = 'first_person'
    else:
        highest_hadith_narrator = 'second_person'
    
    if user_answer == 'a' and highest_hadith_narrator == 'first_person':
        return True,highest_hadith_narrator
    elif user_answer == 'b' and highest_hadith_narrator == 'second_person':
        return True,highest_hadith_narrator
    else:
        return False,highest_hadith_narrator

def initialize():
    first_person, first_person_narrations = random.choice(list(narrators_dict.items()))
    second_person, second_person_narrations = random.choice(list(narrators_dict.items()))

def game():
    # print('\n'*20)
    print(logo)
    narrators_dict = load_data('Day 14/hadith_narrators.csv')


    
    first_person, first_person_narrations = random.choice(list(narrators_dict.items()))
    


    second_person, second_person_narrations = random.choice(list(narrators_dict.items()))
    




    # now let user make a guess, take user guess input
    comparison_result = True
    score  = 0
    while comparison_result:
        print('Compare who has narrated more Hadiths.')
        print(f'A: {first_person}')
        print(vs)
        print(f'B: {second_person}')
        
        user_answer = input("Type 'A' or 'B': ").lower()
        while user_answer not in ['a','b']:
            print('Please choose answer from "A" or "B".')
            user_answer = input("Type 'A' or 'B': ").lower()

        # lets do comparison and give response of who narrated more
        comparison_result, highest_hadith_narrator = compare(first_person_narrations,second_person_narrations,user_answer)
        

        if comparison_result==True:
            score+=1
            if highest_hadith_narrator == 'first_person':
                print(f'Yes you answered correctly. {first_person} narrated more Hadiths than {second_person}')
                print(f'Your current score: {score}')
                
                second_person, second_person_narrations = random.choice(list(narrators_dict.items()))
            else:
                print(f'Yes you answered correctly. {second_person} narrated more Hadiths than {first_person}')
                first_person, first_person_narrations = random.choice(list(narrators_dict.items()))
                print(f'Your current score: {score}')

        else:
            if highest_hadith_narrator == 'first_person':
                print(f'Sorry, {first_person} narrated more Hadiths than {second_person}')
            else:
                print(f'Sorry, {second_person} narrated more Hadiths than {first_person}')
            print(f'Final Score: {score}')
            

            
            # return True
            




game()























