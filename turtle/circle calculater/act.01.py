def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print("The circumference of the circle is:",{round(circumference, 2)})
