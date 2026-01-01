from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass            # Help to move on 

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(Self):
        print("I can bark")
R = Human()
R.move()

k = Snake()
k.move()

r = Dog()
r.move()