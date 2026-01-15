import subprocess
import tkinter as tk
from tkinter import messagebox

def get_password():
    wifi_name = entry.get().strip()

    if not wifi_name:
        messagebox.showwarning("Input Error", "Please enter a Wi-Fi name")
        return

    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", wifi_name, "key=clear"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")

        password = None
        for line in output.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        if password:
            result_label.config(text=f"Password: {password}")
        else:
            result_label.config(text="No password found")

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Wi-Fi profile not found")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Wi-Fi Password Finder")
root.geometry("350x180")
root.resizable(False, False)

tk.Label(root, text="Enter Wi-Fi Name:", font=("Arial", 11)).pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(
    root,
    text="Show Password",
    command=get_password,
    bg="#2e86de",
    fg="white",
    width=20
).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack()

root.mainloop()
