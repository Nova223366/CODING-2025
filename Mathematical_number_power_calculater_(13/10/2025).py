num = int(input("Enter the number: "))
power = int(input("Enter the power of the number: "))
if num <= 0:
    print("What your principal say in morning assamble 'Be positive'.")
elif power <= 0:
    print("Power can't be negative, you are not a super hero.")
    exit()
result = num ** power
print(f"The result of {num} to the power of {power} is {result}")