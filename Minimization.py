import math
#Store epsilon
eps = 10 ** -10
# Store the Golden Ratio
r = (-1.0 + math.sqrt(5)) / 2
#Define a function f(x)
def f(x):
  #return(math.sin(x))
  #return(math.exp(-x) * math.cos(x))
  return(10 * (x ** 6) + (x ** 2) - 3 * x - 2)
#Define a minimization function
def min(a, b, eps):
  x = a + r * (b - a) 
  y = b - r * (b - a)
  u = f(x)
  v = f(y)
  i = 0
  while abs(b - a) > eps:
    if u > v:
      b = x
      x = y
      u = v
      y = b - r * (b - a)
      v = f(y)
    else:
      a = y
      y = x
      v = u
      x = a + r * (b - a)
      u = f(x)
    i += 1
  x = (a + b) / 2
  print("The minima is: (", (a + b) / 2, ", ", f((a + b) / 2), ") Found in ", i, " steps.")

#min(2, 6, eps)
#min(0, math.pi, eps)
min(-2, 2, eps)