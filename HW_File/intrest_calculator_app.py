from tkinter import *

def calculate():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    si = (p * t * r) / 100

    result_label.config(text = "Simple Interest = "+ str(round(si, 2)))

window = Tk()
window.title("Interest Calculator")
window.geometry("400x400")

principal_label = Label(window, text = "Principal Amount:")
principal_label.pack()
principal_entry = Entry(window)
principal_entry.pack()

time_label = Label(window, text = "Time (in years):")
time_label.pack()
time_entry = Entry(window)
time_entry.pack()

rate_label = Label(window, text = "Rate of Interest:")
rate_label.pack()
rate_entry = Entry(window)
rate_entry.pack()

calculate_button = Button(window, text = "Calculate", command = calculate)
calculate_button.pack()
result_label = Label(window, text = "")
result_label.pack()

window.mainloop()