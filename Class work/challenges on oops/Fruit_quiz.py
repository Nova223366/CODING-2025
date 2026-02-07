import random

class FruitQuiz:
    def __init__(self):
        
        self.fruits = {
            "apple": "red",
            "banana": "yellow",
            "grapes": "green",
            "orange": "orange"
        }

    def start_quiz(self):
        print(" Welcome to the Random Fruit Color Quiz\n")

        fruit_list = list(self.fruits.keys())
        

        for fruit in fruit_list:
            user_color = input(f"Enter the color of {fruit}: ").lower()

            if user_color == self.fruits[fruit]:
                print("Correct!\n")
            else:
                print("Wrong!")
                print(f"Correct: {fruit} is {self.fruits[fruit]}\n")


# Main Program
quiz = FruitQuiz()
quiz.start_quiz()
