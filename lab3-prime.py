while True:
     print("Every prime number from the value specified will be listed below.")
     y = input("Insert a number here: ")
     for n in range(2, y+1):
          for x in range(2, n):
              if n % x == 0:
                  print("%s is not a prime number." % n)
                  break
          else:
              print("%s is a prime number." % n)
     while True:
          answer = raw_input("Choose a different value? (y/n): ").lower()
          if answer in ("y", "n", "yes", "no"):
               break
          print("Invalid input.")
     if answer == "y":
          continue
     else:
          print "Goodbye!"
          break
