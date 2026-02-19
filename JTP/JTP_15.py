# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# btn = ttk.Button(root, text="Click Me")
# btn.pack()
# root.mainloop()




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("ttk Example - Student Form")
root.geometry("400x300")

# -----------------------
# Apply Theme
# -----------------------
style = ttk.Style()
style.theme_use("clam")   # You can try: alt, default, classic

# -----------------------
# Variables
# -----------------------
name_var = tk.StringVar()
course_var = tk.StringVar()

# -----------------------
# Labels
# -----------------------
ttk.Label(root, text="Student Registration Form",
          font=("Arial", 14, "bold")).pack(pady=10)

ttk.Label(root, text="Name:").pack(anchor="w", padx=20)
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack(fill="x", padx=20, pady=5)

ttk.Label(root, text="Select Course:").pack(anchor="w", padx=20)

# -----------------------
# Combobox (Dropdown)
# -----------------------
course_combo = ttk.Combobox(root, textvariable=course_var,
                            values=["Python", "Java", "Web Development", "Data Science"])
course_combo.pack(fill="x", padx=20, pady=5)
course_combo.current(0)  # Default selection

# -----------------------
# Button Function
# -----------------------
def submit():
    name = name_var.get()
    course = course_var.get()

    if name == "":
        messagebox.showerror("Error", "Please enter your name")
    else:
        messagebox.showinfo("Success",
                            f"Name: {name}\nCourse: {course}")

# -----------------------
# Submit Button
# -----------------------
ttk.Button(root, text="Submit", command=submit).pack(pady=20)

# Run app
root.mainloop()