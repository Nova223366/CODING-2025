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
