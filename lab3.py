while True:
    from random import *
    x = (randint(1,100))
    print("I've thought of a number between 1 and 100.")
    y = 0
    z = 0
    while x != y:
        y = input("Take a guess: ")
        if y < x:
            print("That's too low.")
        if y > x:
            print("That's too high.")
        z+= 1
    if x == y:
        print("That's correct, well done!")
        print("That took you %s guesses." % z)
    while True:
        answer = raw_input("Play again? (y/n): ").lower()
        if answer in ("y", "n", "yes", "no"):
            break
        print("Invalid input.")
    if answer == "y":
        continue
    else:
        print "Goodbye!"
        break
