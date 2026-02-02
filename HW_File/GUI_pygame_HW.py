from tkinter import *
root = Tk()
root.title("Geeting started with Widgets")
root.geometry("400x300")

lbl1 = Label(root, text = "Enter a number")
lbl1.pack()

num_entry1 = Entry(root)
num_entry1.pack()

lbl2 = Label(root, text = "Multiply by")
lbl2.pack()
num_entry2 = Entry(root)
num_entry2.pack()

text_box = Text(root, height=3)
text_box.pack()

def display():
    number = int(num_entry1.get())
    multiply = int(num_entry2.get())
    result = number * multiply

    text_box.insert(END, f"{result}\n")

btn = Button(root, text="Submit", command=display)
btn.pack()
root.mainloop()