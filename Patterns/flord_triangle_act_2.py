rows = int(input("Please enter the number of rows: "))
number = 1
for i in range(rows):
    for j in range(i + 1):
        print(number, end=" ")
        number = number + 1
    print()