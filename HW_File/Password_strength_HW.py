from tkinter import *
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    strenght = 0
    
    if len(password) >= 8 or password.isupper() or password.islower() or password.isdigit():
        strenght += 4


    if len(password) == 0:
        messagebox.showwarning("Input Error", "Please enter a password.")
    elif strenght == 0:
        strength_label.config(text="Weak", fg="red")
    elif strenght == 3:
        strength_label.config(text="Strong", fg="green")
    else:
        strength_label.config(text="Very Strong", fg="blue")

  
    
root = Tk()
root.geometry("300x200")

root.title("Password Strength Checker")


password_label = Label(root, text="Enter Password:")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

check_button = Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(padx=10, pady=10)

strength_label = Label(root, text="")
strength_label.pack()

root.mainloop()
