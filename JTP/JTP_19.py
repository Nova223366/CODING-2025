from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

root = Tk()
root.title("Restaurant Management System")
root.geometry("600x600")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("clam")

# Custom Styles
style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                padding=6)

style.configure("TLabel",
                background="#1e1e2f",
                foreground="white",
                font=("Segoe UI", 11))

style.configure("Header.TLabel",
                font=("Segoe UI", 18, "bold"),
                foreground="#ffcc00")

# Menu prices in USD
menu_items = {
    "Burger Meal": 3,
    "Pizza Meal": 4,
    "Chicken Meal": 5,
    "Soft Drink": 1,
    "Coffee": 1
}

entries = {}

# Currency Variable
currency_var = StringVar(value="USD")
usd_to_inr = 82  # Example conversion rate


def menu():
    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("500x550")
    menu_window.configure(bg="#2b2b3c")

    ttk.Label(menu_window, text="🍽 MENU", style="Header.TLabel")\
        .grid(row=0, column=0, columnspan=3, pady=20)

    row_num = 1
    for item, price in menu_items.items():
        ttk.Label(menu_window, text=item)\
            .grid(row=row_num, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(menu_window, text=f"${price}")\
            .grid(row=row_num, column=1)

        entry = ttk.Entry(menu_window, width=8)
        entry.grid(row=row_num, column=2)

        entries[item] = entry
        row_num += 1

    # Currency selector
    ttk.Label(menu_window, text="Select Currency:").grid(row=row_num, column=0, pady=15, sticky="w")
    currency_combo = ttk.Combobox(menu_window, textvariable=currency_var, values=["USD", "INR"], state="readonly", width=8)
    currency_combo.grid(row=row_num, column=1)
    currency_combo.current(0)

    row_num += 1

    ttk.Button(menu_window, text="Calculate Total", command=calculate_total)\
        .grid(row=row_num, column=0, pady=25)

    ttk.Button(menu_window, text="Print Receipt", command=print_receipt)\
        .grid(row=row_num, column=1)

    ttk.Button(menu_window, text="Close", command=menu_window.destroy)\
        .grid(row=row_num, column=2)


def calculate_total():
    total = 0
    selected_currency = currency_var.get()

    for item, price in menu_items.items():
        qty = entries[item].get()
        if qty.isdigit():
            cost = int(qty) * price
            if selected_currency == "INR":
                cost *= usd_to_inr
            total += cost

    messagebox.showinfo("Total Bill", f"🔥 {total} {selected_currency}")


def print_receipt():
    receipt = "=========== RECEIPT ===========\n"
    receipt += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    total = 0
    selected_currency = currency_var.get()

    for item, price in menu_items.items():
        qty = entries[item].get()
        if qty.isdigit() and int(qty) > 0:
            cost = int(qty) * price
            if selected_currency == "INR":
                cost *= usd_to_inr
            total += cost
            receipt += f"{item} x{qty} = 🔥 {cost} {selected_currency}\n"

    receipt += "\n-------------------------------\n"
    receipt += f"TOTAL: 🔥 {total} {selected_currency}\n"
    receipt += "Thank you for visiting!\n"

    receipt_window = Toplevel(root)
    receipt_window.title("Receipt")
    receipt_window.geometry("400x400")
    receipt_window.configure(bg="#1e1e2f")

    text = Text(receipt_window,
                font=("Courier New", 11),
                bg="#2b2b3c",
                fg="white")
    text.pack(padx=20, pady=20, fill=BOTH, expand=True)
    text.insert(END, receipt)

    # Save to file
    with open("orders.txt", "a") as file:
        file.write(receipt + "\n\n")

    messagebox.showinfo("Saved", "Order saved successfully!")

def total_earnings():
    try:
        total = 0
        with open("orders.txt", "r") as file:
            for line in file:
                if "TOTAL:" in line:
                    parts = line.split()
                    # parts[-2] is the numeric amount with possible symbols
                    raw_amount = parts[-2]
                    # Remove non-numeric characters except dot
                    amount_str = ''.join(c for c in raw_amount if c.isdigit() or c == '.')
                    amount = float(amount_str)

                    currency = parts[-1]  # currency is the last part
                    # Convert INR to USD if necessary
                    if currency == "INR":
                        amount /= usd_to_inr

                    total += amount
        messagebox.showinfo("Total Earnings", f"💰 Total Earnings: {total:.2f} USD")
    except FileNotFoundError:
        messagebox.showwarning("No Orders", "No orders found yet!")


# Main Window
ttk.Label(root,
          text="🍔 Restaurant Management System",
          style="Header.TLabel").pack(pady=40)

ttk.Button(root, text="Open Menu", command=menu).pack(pady=20)
ttk.Button(root, text="Total Earnings", command=total_earnings).pack(pady=10)
ttk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

root.mainloop()