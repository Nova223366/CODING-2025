
from tkinter import *
import turtle

bg = "purple"

root = Tk()
root.title("User's shape and angle's")
root.geometry("500x500")
root.configure(bg=bg)

lable1 = Label(root, text="Enter your name", bg=bg, fg="white")
lable1.pack()

name_entry = Entry(root, bg="white", fg="black")
name_entry.pack()

root.mainloop()
