import math
epsilon = 10 ** -10

def f(x):
  #return((2 * math.exp(x)) * math.sin(x) + 1)
  #return((x ** 3) * math.cos(x))
  #return((math.exp(-0.01 * x)) * math.sin(0.2 * x))
  return((x ** 10) - (8 * x ** 3) + 2 * x - 0.25)

def bis(a, b, nmax, epsilon):
  fa = f(a)
  fb = f(b)

  if (fa * fb) >= 0:
    print("There is no root between ", a, " and ", b, "!")
    return
  index = 0
  error = b - a
  for i in range(1, nmax + 1):
    error = error / 2
    m = a + error
    fm = f(m)
    if abs(error) < epsilon or abs(fm) < epsilon:
      print("The solution is ", m)
      print(index)
      return()
    if (fa * fm) >= 0:
      a = m
      fa = fm
    else:
      b = m
      fb = fm
    index += 1
#bis(0, 4, 50, epsilon)
#bis(1, 2, 50, epsilon)
#bis(1, 6, 50, epsilon)
bis(-1, 1, 50, epsilon)

    
