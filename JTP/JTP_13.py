from tkinter import *
import turtle

bg = "purple"

root = Tk()
root.title("User's shape and angle's")
root.geometry("500x500")
root.configure(bg=bg)

label1 = Label(root, text="Enter your name", bg=bg, fg="white")
label1.pack()

name_entry = Entry(root, bg="white", fg="black")
name_entry.pack()

label2 = Label(root, text="Enter your shape", bg=bg, fg="white")
label2.pack()

shape_entry = Entry(root, bg="white", fg="black")
shape_entry.pack()

def draw_shape():
    shape = shape_entry.get().strip().lower()

    if shape == "square":
        screen = turtle.Screen()
        screen.bgcolor("orange")
        screen.setup(800, 400)

        square = turtle.Turtle()
        square.color("blue")

        for _ in range(4):
            square.forward(100)
            square.right(90)

    
    else:
        label3 = Label(root, text = "Sorry, only 'square' is supported.", bg=bg, fg="red")
        label3.pack()

btn = Button(root, text="Done", bg="white", fg="black", command=draw_shape)
btn.pack(padx=10, pady=10)

root.mainloop()
