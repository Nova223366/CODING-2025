def factorial(n):
    '''This function recursive function'''
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a number: "))

if num<0:
    print("Factorial does not exist for negative numbers")
else:
    print(factorial.__doc__)
    print("The factorial of", num, "is", factorial(num))
