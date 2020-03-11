import math

def f(x):
  return(3.0 * x + 10.0)
  #return(math.exp(-3.0 * x * x))
  #return(math.sin(x) / x)

def left(a, b, n):
  h = (b - a) / n
  int = 0.0
  for i in range(0, n, 1):
    int += f(a + i * h)
  int *= h
  return(int)

def right(a, b, n):
  h = (b - a) / n
  int = 0.0
  for i in range(1, n + 1, 1):
    int += f(a + i * h)
  int *= h
  return(int)

def trap(a, b, n):
  h = (b - a) / n
  trap = (f(a) + f(b)) / 2.0
  for i in range(1, n, 1):
    trap += f(a + i * h)
  print(h * trap)

x = left(0, 10, 1000)
y = right(0, 10, 1000)
print(((y - x) / 2) + x)
#trap(0, 10, 1000)
