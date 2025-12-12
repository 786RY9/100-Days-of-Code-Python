import pandas as pd
import smtplib
import datetime as dt
import random
from pathlib import Path
import os
from dotenv import load_dotenv


env_path = ".env"
load_dotenv(dotenv_path=env_path)
my_email = os.getenv('my_email')
password = os.getenv("email_pass")


##################### Extra Hard Starting Project ######################

birthdays = pd.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")
# print(birthdays['month'])



# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
cur_month = dt.datetime.now().month
cur_weekday = dt.datetime.now().weekday()
today = (cur_month,cur_weekday)
# print(today)
# print(cur_month,cur_weekday)
# print(birthdays[birthdays['month']==cur_month])
birthday_persons = {(data_row['month'],data_row['day']):data_row for (index,data_row) in birthdays.iterrows()}
# print(birthday_persons[birthday_persons['day']==cur_weekday])
# birthday_persons = birthday_persons[birthday_persons['day']==cur_weekday]
# print(birthday_persons)
if today in birthday_persons:
    # print('yes it is in the file')
    with open(f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt") as letter_template:
        letter = letter_template.read()
        # print(birthday_persons['name'].item())
        b_p = birthday_persons[today]
        # print(b_p)
        letter = letter.replace('[NAME]',b_p['name'])
        
    print(letter)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs='rashidyaseen5484@gmail.com',msg=f"Subject:Happy Birthday\n\n{letter}")


