import tkinter
from tkinter import *


window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

# Label
my_label = tkinter.Label(text="Label text here",font=("Arial",27,"bold"))
my_label.grid(column=0,row=0) # in the center of program, imp to show label, to layout components
my_label.config(padx=50,pady=50)

my_label['text'] = 'new text'
my_label.config(text='latest text')


def button_clicked():
    my_label.config(text='Button got clicked')

def input_field_text_entered():
    my_label.config(text=input.get())





button = Button(text='Click me',command=input_field_text_entered)
button.grid(column=1,row=1)

button2 = Button(text='new button',command=input_field_text_entered)
button2.grid(column=2,row=0)

# Entry component(input field)

input = Entry(width=10,)
input.grid(column=3,row=3)
input.insert(END,string='Some text to begin with')
# print(input.get())
# # Text, textbox(a large area to enter text)
# text = Text(height=5,width=30)
# # puts cursor in textbox
# text.focus()

# # adds some text to begin with
# text.insert(END,"Example of multi-line text entry.")

# # Gets current value in textbox at line 1, character 0
# print(text.get("1.0",END))
# text.pack()

# Spinbox
# def spinbox_used():
    
#     print(spinbox.get())
    
# spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
# spinbox.pack()


# Scale
# called with current scale value.
# def scale_used(value):
#     print(value)
    

# scale = Scale(from_=0,to=100,command=scale_used)
# scale.pack()


# check button 
# def check_button_used():
#     # Prints 1 on button checked otherwise 0
#     print(checked_state.get())

# # Variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# check_button = Checkbutton(text="Is On?",variable=checked_state,command=check_button_used)
# checked_state.get()
# check_button.pack()



# # Radiobuttons

# def radio_used():
#     print(radio_state.get())

# radio_state = IntVar()
# radiobutton1= Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
# radiobutton2= Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# # Listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits=['Apple','Banana','Grapes','Pomegranate','Orange']
# for item in fruits:
#     listbox.insert(fruits.index(item),item)
    
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()




window.mainloop()