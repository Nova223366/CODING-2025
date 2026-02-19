import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")

        self.menu_items = {
            "FRIES MEAL" : 2,
            "BURGER MEAL" : 3,
            "PIZZA MEAL" : 4,
            "CHICKEN MEAL" : 5,
            "SOFT DRINK" : 1,
            "COFFEE" : 1
        }

        self.exchange_rate = 82

        #self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text = "Restaurant Management System", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        self.menu_label = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text = f"{item} (${price})", font=("Arial", 12))

            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_label[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:", font=("Arial", 12)).grid(row=len(self.menu_items)+1, column=0, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, values=["USD", "INR"])

        currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)

        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)

        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)

        order_button.grid(row=len(self.menu_items)+2, column=0, columnspan=2, pady=10)





    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_label.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price:.2f})")

    def place_order(self):
        total_cost = 0
        order_details = []

        for item, entry in self.menu_quantities.items():
            try:
                quantity = int(entry.get())
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                price = self.menu_items[item] * (self.exchange_rate if self.currency_var.get() == "INR" else 1)
                total_cost += price * quantity
                if quantity > 0:
                    order_details.append(f"{item} x {quantity} = {price * quantity:.2f}")
            except ValueError as e:
                messagebox.showerror("Invalid Input", f"Please enter a valid quantity for {item}. {str(e)}")
                return

        if not order_details:
            messagebox.showinfo("No Items", "Please select at least one item to place an order.")
            return

        currency_symbol = "$" if self.currency_var.get() == "USD" else "₹"
        order_summary = "\n".join(order_details) + f"\n\nTotal Cost: {currency_symbol}{total_cost:.2f}"
        messagebox.showinfo("Order Summary", order_summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.geometry("400x400")
    root.mainloop()