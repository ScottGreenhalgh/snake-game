def calculateFibonacci(index):
    if index < 0:
        print "Index cannot be negative."
        return None

    if index <= 1:
        return 1
    
    latest = 1
    previous = 1

    for i in range(2, index + 1):
        latestTemp = latest
        latest += previous
        previous = latestTemp

    return latest

print "Welcome to the Fibonacci Generator!"
print "It will generate the nth number in the Fibonacci sequence for you."
index = input("Enter n: ")
fib = calculateFibonacci(index)
print "K({}) = {}".format(index, fib)
