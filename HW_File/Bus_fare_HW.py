class Vehicle:
    def __init__ (self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare (self):
        return self.seating_capacity*100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenace_charge = base_fare*0.10
        return base_fare + maintenace_charge
bus = Bus(50)

print("Total Bus fare: INR", bus.fare())