from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Adv. Student info")

Header = Label(root, text = "Student ID", font = ("Arial", 20, "bold"))
Header.pack(pady=10)

label1 = Label(root, text = "Name", font = ("Arial", 20, "bold"))
label1.pack()

label1.place(x=60, y=80)

entry1 = Entry(root)
entry1.pack()

entry1.place(x=10, y=120)



root.mainloop()