string = input("Enter your word: ")
character = input("Enter a word you want to: ")
count = 0
<<<<<<< HEAD:Mathematical_number_power_calculater_(13/10/Armstrong_number.py
i = 0
while i < len(string):
    if string[i] == character:
        count += 1
    i += 1  
print(count)
=======
while string.__len__() > count:
    if string[count] == character:
        print(f"Character '{character}' found at index {count}")
    count += 1
print(f"Total occurrences of '{character}': {string.count(character)}")
>>>>>>> afb6fa3d95add71f650efeb4a271d582957fba77:Mathematical_number_power_calculater_(13/10/Character_accurense.py
