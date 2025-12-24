class Employee:
    def __intit__(self):
        print("Employee created")

    def __del__(self):
        print("Employee called")

def Create_obj():
    print("Making object....")
    obj = Employee()
    print("Function end....")
    return obj
print("Calling Create_obj() function....")
obj = Create_obj()
print("Program End....")