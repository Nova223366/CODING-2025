# import turtle

# screen = turtle.Screen()

# name = screen.textinput("Input", "What's your name?")
# print("Hello", name)

# turtle.done()

# import turtle
# screen =turtle.Screen()
# turtle.Screen().bgcolor("orange")
# turtle.Screen().setup(800, 400)
# name = screen.textinput("input", "Enter your name: ")
# age = screen.numinput("input", "Enter your age: ")
# if age < 18:
#     print("You are a minor,", name)
# else:
#     print("You are an adult,", name)
# turtle.bye()


import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(800, 400)

# Create turtle for writing text
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Input
name = screen.textinput("Input", "Enter your name:")
age = screen.numinput("Input", "Enter your age:", minval=0, maxval=120)

# Decide message
if age < 18:
    message = f"You are a minor, {name}"
else:
    message = f"You are an adult, {name}"

# Display message on screen
pen.goto(0, 0)
pen.write(message, align="center", font=("Arial", 24, "bold"))

# Keep window open until clicked
screen.exitonclick()
