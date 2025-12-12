# Even, odd number checker, it will check or provide the under given number 
num = int(input("Enter an number: "))
odd_number = [i for i in range(num) if i % 2 != 0]
even_number = [i for i in range(num) if i % 2 == 0]
print("Odd numbers are:", odd_number)
print("Even numbers are:", even_number)

# Converting fruit first letter into uppercase
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
def convert_uppercase(s):
    return s.capitalize()
uppercase_letters = list(map(convert_uppercase, fruits))
print("\n""Fruits with uppercase first letter:", uppercase_letters,"\n")