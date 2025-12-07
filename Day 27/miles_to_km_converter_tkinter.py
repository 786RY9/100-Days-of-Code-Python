import tkinter
from tkinter import *


def miles_to_km():
    miles = float(input.get())
    ans_km.config(text=round(miles*1.60934,2))

window = tkinter.Tk()
window.minsize(width=200,height=200)
window.title('Mile to Km Converter')
window.config(padx=50,pady=50)


input = Entry(width=10)
input.grid(column=1,row=0)
miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0,row=1)

ans_km = Label(text='0')
ans_km.grid(column=1,row=1)

km_label = Label(text='Km')
km_label.grid(column=2,row=1)

calculate_btn = Button(text='Calculate',command=miles_to_km)
calculate_btn.grid(column=1,row=2)








window.mainloop()









