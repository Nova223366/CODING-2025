from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(mater = root, height=200, width = 360, bg = 'white')

labl1 = Label(frame, text = "Full Name", bg = 'lightblue', fg = 'black', width = 12)
labl2 = Label(frame, text = "Email Id", bg = 'lightblue', fg = 'black', width = 12)
labl3 = Label(frame, text = "Enter Password", bg = 'lightblue', fg = 'black', width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = '*')

def display():
    name = name_entry.get()
    greet = "Welcome " + name
    massage = "\n"