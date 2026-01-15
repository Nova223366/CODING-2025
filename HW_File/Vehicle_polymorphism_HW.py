# class Breed:
#     def __init__ (self, breed, colour, size, funfact):
#         self.breed = breed
#         self.colour = colour
#         self.size = size
#         self.funfact = funfact
#     def display_info(self):
#         print("Breed:", self.breed)
#         print("Colour:", self.colour)
#         print("Size:", self.size)
#         print("Fun Fact:", self.funfact)
# dog1 = Breed("Labrador Retriever", "Yellow", "Large", "Labradors are known for their friendly nature and are often used as guide dogs.")
# dog2 = Breed("Beagle", "Tricolor", "Medium", "Beagles have an excellent sense of smell and are often used in detection work.")
# dog1.display_info()
# print("\n")
# dog2.display_info()

class BMW:
    def __init__ (self, Model, Fuel_type, max_speed, limited_Top_speed):
        self.Model = Model
        self.Fuel_type = Fuel_type
        self.max_speed = max_speed
        self.limited_Top_speed = limited_Top_speed
    def display_info(self):
        print("Model:", self.Model)
        print("Fuel Type:", self.Fuel_type)
        print("Max Speed:", self.max_speed)
        print("Limited Top Speed:", self.limited_Top_speed)
class ferrari:
    def __init__ (self, Model, Fuel_type, max_speed, limited_Top_speed):
        self.Model = Model
        self.Fuel_type = Fuel_type
        self.max_speed = max_speed
        self.limited_Top_speed = limited_Top_speed
    def display_info(self):
        print("Model:", self.Model)
        print("Fuel Type:", self.Fuel_type)
        print("Max Speed:", self.max_speed)
        print("Limited Top Speed:", self.limited_Top_speed)
BMWinfo = BMW("BMW M4 CS", "petrol", "300+ km/h", "250 km/h")
ferrari1 = ferrari("488 GTB", "Petrol", "330 km/h", "310 km/h")
BMWinfo.display_info()
print("\n")
ferrari1.display_info()
