while True:
    name = input("Enter your name: ").title()
    age = int(input("Enter your age: "))
    if name == "Saqib":
        print("Hello, how are you ", name)
        print("You has enter your age ",age +10)
        print(f"Your name as {len(name)} characters")
    else:
        print(name)
    