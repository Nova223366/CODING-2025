class Vechicle:

    def __init__ (self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vechicle):

    #pass
    def display(self):
        print("Inheritance")
School_Bus = Bus("Schoolc Volvo", 180, 12)
print("Vehicle Name:", School_Bus.name, "Speed:", School_Bus.max_speed, "Milage:", School_Bus.milage)