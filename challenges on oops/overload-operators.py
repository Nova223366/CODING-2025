class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is not less than ob1"
        
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
        
ob1 = A(5)
ob2 = A(6)
print("Passed Value: ", ob1.a, ob2.a)
print(ob1 < ob2)
ob3 = A(66)
ob4 = A(99)
print("Passed Value: ", ob3.a, ob4.a)
print(ob3 == ob4)