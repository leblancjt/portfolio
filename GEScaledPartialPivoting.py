from math import sqrt

def GE_SPP(A, b):
  n = len(A) # if not built-in in a language,
  # read in n as the third argument
  L = [i for i in range(n)] # a quick way to initialize L
  x = [0.0 for i in range(n)]
  S = [0.0 for i in range(n)]
  # build the S vector
  for i in range(0, n - 1): # find largest element in each row of a
    for j in range(0, n - 1):
      if (abs(A[i][j]) > S[i]):
        S[i] = abs(A[i][j])
# could calculate cond = the product of the two-norms of the rows of A here
  cond = 1
  for i in range(0, n):
    sum = 0
    for j in range(0, n):
      sum += A[i][j] ** 2
    cond *= sqrt(sum)
  #forward elimination
  for k in range(n - 1):
    # check to see whether we need to swap rows
    R = 0.0
    for i in range(k, n - 1):
      temp = abs(A[L[i]][k] / S[L[i]])
      if temp > R:
        R = temp
        index = i
    # do the swap
    temp = L[index]
    L[index] = L[k]
    L[k] = temp
    # zero out below the diagonal (update both a and b)
    for i in range(k + 1, n):
      xmult = A[L[i]][k] / A[L[k]][k]
      for j in range(k + 1, n):
        A[L[i]][j] -= xmult * A[L[k]][j]
      b[L[i]] -= xmult * b[L[k]]

# could divide cond by the absolute values of the pivots here
  pivots = 1
  for i in range(0, n):
    pivots *= abs(A[L[i]][i])
  cond = cond / pivots

  #back substitution
  x[n - 1] = b[L[n - 1]] / A[L[n - 1]][n - 1]
  for k in range(n - 2, -1, -1):
    sum = b[L[k]]
    for j in range(k + 1, n):
      sum -= A[L[k]][j] * x[j]
    x[k] = sum / A[L[k]][k]

  print(x)
  #also output cond!
  print(cond)

A = [[1, 1, 1, 1, 1], [1, 3, 9, 27, 81], [1, 7, 49, 343, 2401], [1, 10, 100, 1000, 10000], [1, 14, 196, 2744, 38416]]
b = [22, 1, -2, 12, -2]
GE_SPP(A, b)