
from tkinter import *
import turtle

def draw_shape(shape_entry):
   import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(800, 400)
square = turtle.Turtle()
square.color("blue")
for _ in range(4):
    square.forward(100)
    square.right(90)

bg = "purple"

root = Tk()
root.title("User's shape and angle's")
root.geometry("500x500")
root.configure(bg=bg)

lable1 = Label(root, text="Enter your name", bg=bg, fg="white")
lable1.pack()

name_entry = Entry(root, bg="white", fg="black")
name_entry.pack()

lable2 = Label(root, text="Enter your shape", bg=bg, fg="white")
lable2.pack()
shape_entry = Entry(root, bg = "white", fg="black")
shape_entry.pack()

btn = Button(root, text = "Done", bg = "white", fg = "black", command = lambda: draw_shape(shape_entry.get()))
btn.pack()

root.mainloop()