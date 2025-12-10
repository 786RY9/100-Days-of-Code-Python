# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

def generate_p():
    password_input.delete(0,END)
    generated_password = generate_password()
    # print(generated_password)
    password_input.insert(END,string=generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website= website_input.get()
    username_email = email_or_username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email":username_email,
            "password": password
        }
    }
    if len(password) < 8:
        messagebox.showinfo(title="Oops",message="Password must have a length of 8 characters.")
    elif len(website)==0 or len(username_email)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any field empty.")
        
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {username_email}\nPassword: {password}\nIs it ok to save?")
        
        if is_ok:
            
            try:
                with open('/home/ry/Pictures/100 days of Python/data.json',mode='r') as file:
                    # json.dump(new_data,file,indent=4)
                    #Reading old data
                    data = json.load(file)
                    # print(data)
                    
                    
            except FileNotFoundError:
                print('File does not exists. Creating File and writing data to it.')
                with open('/home/ry/Pictures/100 days of Python/data.json',mode='w') as file:
                # saving updated data
                    json.dump(new_data,file,indent=4)
            else:
                # updating old data with new data
                data.update(new_data)
                with open('/home/ry/Pictures/100 days of Python/data.json',mode='w') as file:
                    json.dump(data,file,indent=4)
                
            finally:
                
                # file.write(f"{website} | {username_email} | {password}\n")

                website_input.delete(0,END)
                
                password_input.delete(0,END)


def search():
    website = website_input.get()

    try:
        with open("/home/ry/Pictures/100 days of Python/data.json","r") as file:
            data = json.load(file)
    
    except FileNotFoundError:
        print('Data file does not exist')
        messagebox.showinfo(title='error',message='No Data File present.')
    else:
        if website not in data:
            messagebox.showinfo(title='error',message='No such website data exists.')
        else:
            print(data)
            email = data[website]['email']
            password = data[website]['password']
            
            messagebox.showinfo(title="Data",message=f"email: {email}\n password: {password}")
        
# ---------------------------- UI SETUP ------------------------------- #

import tkinter
from tkinter import *


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.config(bg='white')

canvas = Canvas(width=200,height=200,bg='white',highlightthickness=0)
image = PhotoImage(file="Day 29/password-manager-start/logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ",bg='white')
website_label.grid(column=0,row=1)

website_input = Entry(width=30,bg='white')
website_input.focus()
website_input.grid(column=1,row=1)

search_btn = Button(text='Search',command=search,bg='white',width=13)
search_btn.grid(column=2,row=1)

email_or_username_label = Label(text="Email/Username: ",bg='white')
email_or_username_label.grid(column=0,row=2)

email_or_username_input = Entry(width=48,bg='white')
email_or_username_input.insert(0, 'ry9@gmail.com')
email_or_username_input.grid(column=1,row=2,columnspan=2)

password_label = Label(text='Password: ',bg='white')
password_label.grid(column=0,row=3)

password_input = Entry(width=30,bg='white')
password_input.grid(column=1,row=3)

generate_password_btn = Button(text="Generate Password",bg='white',width=13,command=generate_p)

generate_password_btn.grid(column=2,row=3)

add_btn = Button(text="Add",width=36,bg='white',command=save)
add_btn.grid(column=1,row=4,columnspan=2)


window.mainloop()

