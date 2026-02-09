from tkinter import *
import turtle

bg = "purple"

root = Tk()
root.title("User's shape and angle's")
root.geometry("500x500")
root.config(bg=bg)

lable1 = Label(root, text = "Enter your name",
bg = bg, fg="white")
lable1.pack()
name_entry = Entry(root)
name_entry.pack()

lable2 = Label(root, text = "Enter what angle you want",bg = bg, fg = "white")
lable2.pack()
angle_entry = Entry(root)
angle_entry.pack()

def display():
    name = name_entry.get()
    angle = angle_entry.get()
    text_box.insert(END,f"{name}, you type {angle} to draw\n")

btn = Button(root, text = "Start", command = display)
btn.pack()

text_box = Text(root, height = 8)
text_box.pack()

'''if angle_entry == square:
    turtle.Screen().bgcolor("orange")
    turtle.Screen().setup(800, 400)
    square = turtle.Turtle()
    square.color("blue")
    for _ in range(4):
        square.forward(100)
        square.right(90)
'''

root.mainloop()
