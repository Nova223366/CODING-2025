import tkinter as tk
import random

# Create window
window = tk.Tk()
window.title("Rock Paper Scissors App")
window.geometry("400x400")

# List of choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    # Game rules
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Display result
    result_label.config(
        text=f"Your Choice: {user_choice}\nComputer Choice: {computer_choice}\n\n{result}"
    )

# Title Label
title_label = tk.Label(window, text="Rock Paper Scissors Game", font=("Arial", 14))
title_label.pack(pady=20)

# Buttons
rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run window
window.mainloop()