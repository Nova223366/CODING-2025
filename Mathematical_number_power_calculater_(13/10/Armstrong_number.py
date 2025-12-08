string = input("Enter your word: ")
character = input("Enter a word you want to: ")
count = 0
i = 0
while i < len(string):
    if string[i] == character:
        count += 1
    i += 1  
print(count)
