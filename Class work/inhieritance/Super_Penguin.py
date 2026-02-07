# Parent class
class Bird:

    def __init__(self):
        print("Bird is ready")
    def who_is_this(self):
        print("Bird")
    def swim(self):
        print("swim faster")

# Child class
class Penguin (Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("Run faster")
peggy = Penguin()
Bird.who_is_this(peggy)               # For bird like Situation method
peggy.who_is_this()
peggy.swim()
peggy.run()