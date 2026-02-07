from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='white')
frame.place(x=20, y=0)

# Labels
labl1 = Label(frame, text="Full Name", bg='lightblue', fg='black', width=12)
labl2 = Label(frame, text="Email Id", bg='lightblue', fg='black', width=12)
labl3 = Label(frame, text="Enter Password", bg='lightblue', fg='black', width=12)

labl1.place(x=10, y=20)
labl2.place(x=10, y=70)
labl3.place(x=10, y=120)

# Entry fields
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show='*')

name_entry.place(x=150, y=20)
email_entry.place(x=150, y=70)
pass_entry.place(x=150, y=120)

# Textbox
textbox = Text(root, height=5, width=45)
textbox.place(x=20, y=200)

def display():
    textbox.delete(1.0, END)
    name = name_entry.get()
    greet = "Welcome " + name
    message = "\nCongratulations! You have successfully logged in."
    textbox.insert(END, greet)
    textbox.insert(END, message)

# Button
btn = Button(frame, text="Create account", bg='lightblue',
             fg='black', width=12, command=display)
btn.place(x=130, y=170)

root.mainloop()
