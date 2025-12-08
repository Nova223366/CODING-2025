import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(800, 400)
square = turtle.Turtle()
square.color("blue")
for _ in range(4):
    square.forward(100)
    square.right(90)
