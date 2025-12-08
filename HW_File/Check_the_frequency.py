test_dictionary = {"Codingal": 3, "is": 2, "best": 2, "for": 2, "Coding": 1}

print(test_dictionary)

user_input = int(input("Enter the frequency do you want to check: "))

frequency_count = 0
for i in test_dictionary.values():
    if i == user_input:
        frequency_count += 1
print(frequency_count)