def name_checker(name):
    if name in list:
        return "You were in list"
    else:
        return "You were not in list"
list = ["Rohin", "Aditya", "Aman", "Sammar"]
name = input("Enter your name: ").capitalize()
result = name_checker(name)
print(result, name)
