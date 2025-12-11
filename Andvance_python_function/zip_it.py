s1 = {2, 3, 1, 76, 22}
s2 = {1, 5, 9, 8, 7}
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stock = ["Relince", "infosys", "tcs"]
prices = [2175, 1127, 2750]

new_dict = {stock: prices for stock,       prices in zip(stock, prices)}
print("\n{}".format(new_dict)) # print("\n",new_dict)