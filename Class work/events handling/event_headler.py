from tkinter import *

window = Tk()
window.title("Event handling")
window.geometry("100x100")

def handle_keypress(event):
    """Print the character associated with the key pressed."""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    """Print the coordinates of the mouse click."""
    print("\nThe button was clicked!")

button = Button(text = "Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()