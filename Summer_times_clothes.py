tem = int(input("Enter the temperature in Celsius: "))
if tem > 30:
    print(f"The temperature is {int (tem)}° means it's a hot day, wear light clothes.")
elif 20 <= tem <= 30:
    print(f"The temperature is {int (tem)}° ♥ means it's a warm day, wear a t-shirt and shorts.")
elif 10 <= tem < 20:
    print(f"The temperature is {int (tem)}° ♥ means it's a cool day, wear a light jacket.")
else:
    print(f"The temperature is {int (tem)}° means it's cold, wear a warm coat and scarf.")
