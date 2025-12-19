class Breed:
    def __init__ (self, breed, colour, size, funfact):
        self.breed = breed
        self.colour = colour
        self.size = size
        self.funfact = funfact
    def display_info(self):
        print("Breed:", self.breed)
        print("Colour:", self.colour)
        print("Size:", self.size)
        print("Fun Fact:", self.funfact)
dog1 = Breed("Labrador Retriever", "Yellow", "Large", "Labradors are known for their friendly nature and are often used as guide dogs.")
dog2 = Breed("Beagle", "Tricolor", "Medium", "Beagles have an excellent sense of smell and are often used in detection work.")
dog1.display_info()
print("\n")
dog2.display_info()