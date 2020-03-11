# Author: John LeBlanc
# Date: 2/21/2020

import math

def f(x):
  #return math.exp(0.2 * x) - x ** 2
  return x ** 3 - 3 * x ** 2 + 3 * x - 1 

def fp(x):
  #return 0.2 * math.exp(0.2 * x) - 2 * x
  return 3 * x ** 2 - 6 * x + 3

def bisec(a, b, max, tol):
  fa = f(a)
  fb = f(b)
  if (fa * fb) > 0:
    return 'There is no root between ' + str(a) + ' and ' + str(b)
  d = b - a

  for i in range(1, max + 1):
    d /= 2
    m = a + d
    fm = f(m)
    if fm == 0 or abs(d) < tol:
      print(str(m))
      return 'Convergence at ' + str(i) + ' iterations'
    if (fa * fm) > 0.0:
      a = m
      fa = fm
    else:
      b = m
      fb = fm

def sec(a, b, max, tol):
  fa = f(a)
  fb = f(b)
  if abs(fa) > abs(fb):
    c = a
    a = b
    b = c
    fc = fa
    fa = fb
    fb = fc
  
  for i in range(1, max + 1):
    d = (b - a) / (fb - fa)
    b = a
    fb = fa
    d *= fa
    a -= d
    fa = f(a)
    if fa == 0 or abs(d) < tol:
      print(str(a))
      return 'Convergence at ' + str(i) + ' iterations'
    if abs(fa) > abs(fb):
      c = a
      a = b
      b = c
      fc = fa
      fa = fb
      fb = fc

def newt(x, max, tol, mult):
  fx = f(x)

  for i in range(1, max + 1):
    fpx = fp(x)
    if abs(fpx) == 0:
       return 'There is no root.'
    d = fx / fpx
    x -= mult * d
    fx = f(x)
    if fx == 0 or abs(d) < tol:
      print(str(x))
      return 'Convergence in ' + str(i) + ' iterations'
  return ('Convergence did not occur after ' + str(max) + ' Iterations.')

tol = 10 ** -10
max = 100
'''
print('Bisection Root Approximation:\n')
print(bisec(-5, 0, max, tol))
print(bisec(0, 5, max, tol))
print(bisec(30, 40, max, tol))
print('\nSecant Root Approximation:\n')
print(sec(-5, 0, max, tol))
print(sec(0, 5, max, tol))
print(sec(30, 40, max, tol))
print('\nNewton Root Approximation:\n')
print(newt(-5, max, tol))
print(newt(0, max, tol))
print(newt(1, max, tol))
print(newt(30, max, tol))
'''
x = 4
mult = [1, 2, 3]
for m in mult:
  print(newt(x, max, tol, m))
