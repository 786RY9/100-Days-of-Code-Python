import pandas as pd
import csv

# We need list of celebrities or things with number of followers they have, it could from a csv file. At first choose 2 from that csv at random 
df = pd.read_csv('Day 14/hadith_narrators.csv')
with open('Day 14/hadith_narrators.csv',newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader) # skipping header
    for row in csv_reader:
        print(row[0] + "      " + row[1])




# now let user make a guess, take user guess input



# compare users guess with actual data that we have if true then add +1 score 



# now keep that celeb or thing that has more numbers and inplace of other choose some other thing or celeb at random from csv and display and again users_input



 
# else stop and give user an option to play again along with users score


























