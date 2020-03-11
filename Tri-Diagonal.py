# Author: John LeBlanc
# Date: 03/06/2020
from math import exp

def createList(A, i):
  n = len(A)
  if i == 0:
    d = []
    for j in range(n):
      d.append(A[j][j])
    return d
  if i == -1:
    a = []
    for j in range(1, n):
      a.append(A[j][j + i])
    return a
  if i == 1:
    c = []
    for j in range(n - 1):
      c.append(A[j][j + i])
    return c

def buildMatrix(t, n):
  h = (t[1] - t[0]) / n
  a = t[0]
  t = [(a + i * h) for i in range(n + 1)]
  a = [-(1 + h / 2) for i in range(n - 1)]
  b = [(-h ** 2) * exp(t[i] - 1) for i in range(n)]
  c = [-(1 - h / 2) for i in range(n - 1)]
  d = [(2 + h ** 2) for i in range(n)]

  A = [[0.0 for i in range(n)] for i in range(n)]
  for i in range(n):
    A[i][i] = d[i]
    if i != 0:
      A[i][i - 1] = a[i - 1]
    if i < n - 1:
      A[i][i + 1] = c[i]
  return A, b

def tri(a, b, c, d):
  n = len(b)
  x = [0.0 for i in range(n)]
  h = 2 / n

  for i in range(2, n):
    xmult = a[i - 1] / d[i - 1]
    d[i] -= xmult * c[i - 1]
    b[i] -= xmult * b[i - 1]
  x[n - 1] = b[n - 1] / d[n - 1]
  for i in range(n - 2, -1, -1):
    x[i] =  (b[i] - c[i] * x[i + 1]) / d[i]
  xp = []
  xdp = []
  for i in range(1, n - 1):
    xp.append((x[i + 1] - x[i - 1]) / 2 * h)
    xdp.append((x[i - 1] - 2 * x[i] + x[i + 1]) / h ** 2)
  print(x)
  return x, xp, xdp

t = [0, 2]
n = 8
A = buildMatrix(t, n)[0]
a = createList(A, -1)
b = buildMatrix(t, n)[1]
c = createList(A, 1)
d = createList(A, 0)

tri(a, b, c, d)