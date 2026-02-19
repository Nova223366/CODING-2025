from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Student info")

def submit():

    if entry.get() == "" and entry2.get() == "" and entry3.get() == "" and entry4.get() == "" and entry5.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
         root = Tk()
    root.geometry("200x200")
    root.title("Student info")

    name = entry.get()
    age = entry2.get()
    class_ = entry3.get()
    section = entry4.get()
    roll_no = entry5.get()

    label_name = Label(root, text = f"Name: \t{name}")
    label_name.pack()
    label_age = Label(root, text = f"Age: \t{age}")
    label_age.pack()
    label_class = Label(root, text = f"Class: \t{class_}")
    label_class.pack()
    label_section = Label(root, text = f"Section: \t{section}")
    label_section.pack()
    label_roll_no = Label(root, text = f"Roll No: \t{roll_no}")
    label_roll_no.pack()

    btn = Button(root, text = "Close", command = root.destroy)
    btn.pack(pady=10)

    root.mainloop()

label1 = Label(root, text = "Name")
label1.pack()
entry = Entry(root)
entry.pack()

label2 = Label(root, text = "Age")
label2.pack()
entry2 = Entry(root)
entry2.pack()

label3 = Label(root, text = "class")
label3.pack()
entry3 = Entry(root)
entry3.pack()

label4 = Label(root, text = "Section")
label4.pack()
entry4 = Entry(root)
entry4.pack()

label5 = Label(root, text = "Roll no")
label5.pack()
entry5 = Entry(root)
entry5.pack()

btn = Button(root, text = "Submit", command=submit)
btn.pack(padx=1, pady=10)

btn = Button(root, text = "Close", command = root.destroy)
btn.pack()

root.mainloop()