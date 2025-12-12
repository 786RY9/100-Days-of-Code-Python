import datetime as dt
import random
import smtplib
from pathlib import Path
from dotenv import load_dotenv
import os


current_dir = Path(__file__).parent
dotenv_path = '.env'
# print(os.listdir(dotenv_path))
# print("dotenv path: ", dotenv_path)
# print("current directory: ", current_dir)
load_dotenv(dotenv_path=dotenv_path)
email_pass = os.getenv("email_pass")
my_email = os.getenv("my_email")
password = email_pass
# print(email_pass)
# print(my_email)
today = dt.datetime.now().weekday()
if today == 1:
    with open("Day 32/quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
        
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs='rashidyaseen5484@gmail.com',msg=f"Subject:Monday Motivation\n\n{quote}".encode('utf-8'))




















