list1 = [1, 2, 3]
list2 = [4, 5, 6, 8] # Number 8 will ignored becuase the there is no partner form him (For examle only)
result = map(lambda x, y: x + y, list1, list2)
print("Addition of two lists")
print(list(result))

# using map
num = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
squre = list(map(sq, num))
print("Square of the list is:")
print(squre)