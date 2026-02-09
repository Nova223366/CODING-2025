from tkinter import *
import datetime
root = Tk()
root.title("Age calculator app")
root.geometry("500x500")

lable1 = Label(root, text = "Enter your name")
lable1.pack()
name_entry = Entry(root)
name_entry.pack()

lable2 = Label(root, text = "Enter your birth date")
lable2.pack()
date_entry = Entry(root)
date_entry.pack()

lable3 = Label(root, text = "Enter your birth month")
lable3.pack()
month_entry = Entry(root)
month_entry.pack()

lable4 = Label(root, text = "Enter your birth year")
lable4.pack()
year_entry = Entry(root)
year_entry.pack()


def display():
    name = name_entry.get()
    date = int(date_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    current_year = datetime.datetime.now().year
    age = current_year - year
    text_box.insert(END,"\t"f"{name}, your age is {age}\n")

btn = Button(root, text="Submit", command=display)
btn.pack() 

text_box = Text(root, height=5)
text_box.pack()
root.mainloop()