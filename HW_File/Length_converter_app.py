from tkinter import *

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text = "Centimeters: " + str(cm))

root = Tk()
root.title("Length converter app")
root.geometry("400x400")

label1 = Label(root, text = "Enter length in inches:")
label1.pack()

entry = Entry(root)
entry.pack()
btn = Button(root, text="Convert", command=convert)
btn.pack()

result = Label(root, text = "")
result.pack()

root.mainloop()