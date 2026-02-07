num = int(input("Enter your nuber: "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1

print(f"The sum of natural number up to {num} is {sum}")

temp = num

while temp > 0:

digit = temp % 10

sum += digit ** 3

temp //= 10