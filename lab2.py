while True:
    from random import *
    ValueOne = randint(2, 10)
    ValueTwo = randint(2, 10)
    x = input("What is %s X %s? " % (ValueOne, ValueTwo))
    if x == ValueOne*ValueTwo :
        print("Correct!")
    else:
        print("Incorrect")
    while True:
        answer = raw_input("Would you like to play again? (y/n): ").lower()
        if answer in ("y", "n", "yes", "no"):
            break
        print("Invalid input.")
    if answer == "y":
        continue
    else:
        print "Goodbye!"
        break

