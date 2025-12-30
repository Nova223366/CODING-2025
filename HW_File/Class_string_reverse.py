class String:
    def __init__(self, user_input=""):
        self.user_input = user_input

    def reverse(self):
        return self.user_input[::-1]


word = input("Enter a word: ")
obj = String(word)
print("Reversed string:", obj.reverse())
