class Personal (object):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name)
        print(self.id_number)

class Employee (Personal):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        Personal.__init__(self, name, id_number)

a = Employee("Rohan", 886012, 200000, "Intern")
a.display()