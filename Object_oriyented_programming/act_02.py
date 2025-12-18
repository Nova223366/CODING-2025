class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.milage = mileage
        print(max_speed)

    def display(self): # if you want to show it again 
        print("Max Speed:", self.max_speed)

modelX = Vehicle(250, 12)
modelX.display()

print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:",modelX.milage)