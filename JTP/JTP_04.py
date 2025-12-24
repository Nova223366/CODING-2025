import turtle
x = int(input("Tell the Number of sides ya need: ""\n"))
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(800, 400)
y=360/x
shape = turtle.Turtle()
shape.color("blue")
for _ in range(x):
    shape.forward(100)
    shape.right(y)  

