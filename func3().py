def func1():
    print("Inside Func1")
    return 10

def func2():
    print("Inside Func2")
    num = func1()  # Calls func1
    return num

def func3():
    print("Inside Func3")
    num = func2()  # Calls func2, which in turn calls func1
    num = num * 5  # Multiplies the returned value (10) by 5
    return num

val = func3()
print(val)
