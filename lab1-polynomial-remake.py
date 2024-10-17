def readPolynomial():
  return map(
    (lambda x: float(input("Please enter a value for " + x + ". "))),
    ['a', 'b', 'c', 'm', 'n', 'o']
  )

a, b, c, m, n, o = readPolynomial()

def differentiate(a, b, c, m, n, o):
  return [a * m, b * n, c * o, m - 1, n - 1, o - 1]

def integrate(a, b, c, m, n, o):
  return [a / (m + 1), b / (n + 1), c / (o + 1), m + 1, n + 1, o + 1]
  
def yIntercept(a, b, c, m, n, o):
  return (a**m)+(b**n)+(c**o)

def outputPolynomial(a, b, c, m, n, o, type = ""):
  print("The " + type + "polynomial is: %sx^%s + %sx^%s + %sx^%s" %(a, m, b, n, c, o))
  
Da, Db, Dc, Dm, Dn, Do = differentiate(a, b, c, m, n, o)
outputPolynomial(Da, Db, Dc, Dm, Dn, Do, "differentiated ")
Ia,Ib, Ic, Im, In, Io = integrate(a, b, c, m, n, o)
outputPolynomial(Ia, Ib, Ic, Im, In, Io, "integrated ")

y = yIntercept(a, b, c, m, n, o)
print("The y-intercept for the polynomial is %s." %(y))
 
