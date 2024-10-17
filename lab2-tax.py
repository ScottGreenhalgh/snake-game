amount = float(input("How much did you make this year? "))
taxtotal = 0
newamount = 0
if amount > 150000:
    difference = amount - 150000
    newamount = amount - difference
    taxtotal += (difference * 0.45)

if amount > 32000 and amount <= 150000:
    difference = amount - 32000
    newamount = amount - difference
    taxtotal += (difference * 0.4)

if amount > 11000 and amount <= 32000:
    difference = amount - 11000
    taxtotal += (difference * 0.2)

print("Your total tax is %s" % (taxtotal))
