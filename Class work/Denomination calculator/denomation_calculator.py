from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination calculator")
root.geometry("650x400")
root.config(bg="light grey")

# Add image (use correct path or remove if not needed)
upload = Image.open(r"C:\CODING 2025\Class work\Denomination calculator\images.png")
upload = upload.resize((500, 400))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg = "light grey")
label.place(x=80, y=120)

label1 = Label(root, text="Hey User! Welcome to Denomination Calculator", bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    messagebox.showinfo("Alert", "Do you want to calculate the denomination?")
    topwin()

button1 = Button(root, text="Let's get started", command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination calculator")
    top.config(bg="light grey")
    top.geometry("600x350+50+50")

    label1 = Label(top, text="Enter total amount", bg="light blue")
    entry = Entry(top)

    lb1 = Label(top, text="Here are number of notes for each denomination", bg="light grey")

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, note2000)
            t2.insert(0, note500)
            t3.insert(0, note100)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    btn = Button(top, text="Calculate", command=calculate, bg="brown", fg="white")

    label1.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)

    lb1.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

root.mainloop()
