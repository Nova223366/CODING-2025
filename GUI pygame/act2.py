from tkinter import *
from datetime import date

root = Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')

# Add widgets 
# Add label

lbl = Label(text = "Hey There", fg = "white", bg = "blue", height=1, width = 300 )

name_lbl = Label(text = "Full name", bg = "Yellow") 
name_entry = Entry()

def display():
    name = name_entry.get()
    global massage
    massage = "Welcome to the Application \nToday's date is: " 
    greet = "Hello, "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, massage)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text = "Submit", command= display, bg = "green", fg = "white")

lbl.pack()
name_entry.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()