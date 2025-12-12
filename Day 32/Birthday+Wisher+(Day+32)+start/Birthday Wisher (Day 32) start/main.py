import smtplib
from pathlib import Path
from dotenv import load_dotenv
import os

current_dir = Path(__file__).parent
dotenv_path = current_dir.parent / '..' /'..'/'.env'
# print(os.listdir(dotenv_path))
# print("dotenv path: ", dotenv_path)
# print("current directory: ", current_dir)
load_dotenv(dotenv_path=dotenv_path)
email_pass = os.getenv("email_pass")
my_email = os.getenv("my_email")
password = email_pass

qoutes_path = "Day 32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt"

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,to_addrs='rashidyaseen5484@gmail.com',msg='Subject:Happy Birthday Bro from Rashid Yaseen\n\nHappy Birthday Bro\n\nRashid Yaseen'
        )


import datetime as dt


print(dt.datetime.now())
now = dt.datetime.now()
year = now.year
print(year)


# if now.month == 12:
#     print('Dec')
dob = dt.datetime(year=2002,month=6,day=6)
print(dob)





