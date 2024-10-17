def factorial(y):
    x=1
    for i in range(1,y+1):
        x*=i
    return x
y = input("Select a value: ")
factorial(y)
print(factorial(y))
