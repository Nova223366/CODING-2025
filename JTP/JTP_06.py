class commerce:
    def __init__ (self, Class, Section, Total_student, Girls, Boyes):
        self.Class = Class
        self.Section = Section
        self.Total_student = Total_student
        self.Girls = Girls
        self.Boyes = Boyes

    def display_info(self):
        print("Class:", self.Class)
        print("Section:", self.Section)
        print("Total Student:", self.Total_student)
        print("Girls:", self.Girls)
        print("Boyes:", self.Boyes)
info = commerce( "11", "Commerce", "22", "8", "14")
print("\n")
info.display_info()
print("\n")