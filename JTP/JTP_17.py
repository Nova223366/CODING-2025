from tkinter import *

root = Tk()
root.title("Restaurant Management System")
root.geometry("500x500")


# Placeholder function
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def menu():
    menu_items = {
        "Burger Meal": 3,
        "Pizza Meal": 4,
        "Chicken Meal": 5,
        "Soft Drink": 1,
        "Coffee": 1
    }

    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("400x400")

    row_num = 0

    for item, price in menu_items.items():
        label = Label(menu_window, text=f"{item}: ${price}", font=("Arial", 12))
        label.grid(row=row_num, column=0, padx=10, pady=5, sticky="w")

        entry = Entry(menu_window, width=10)
        entry.grid(row=row_num, column=1, padx=10, pady=5)

        add_placeholder(entry, "Qty")

        row_num += 1

    btnc = Button(menu_window, text="Close", command = menu_window.destroy)
    btnc.grid(row=row_num, column=0, columnspan=2, pady=20)


label1 = Label(root, text="Welcome to the Restaurant Management System",
               font=("Arial", 14, "bold"))
label1.pack(pady=20)

btn = Button(root, text="Show menu", font=("Arial", 12, "bold"), command=menu)
btn.pack(pady=10)

root.mainloop()