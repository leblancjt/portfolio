def GE(A, b):
  x = [0, 0, 0]
  n = len(b)
  for k in range(0, n - 1):
    for i in range(k + 1, n):
      for j in range(k + 1, n):
        A[i][j] -= (A[i][k] / A[k][k]) * A[k][j]
      b[i] -= (A[i][k] / A[k][k]) * b[k]

  x[n - 1] = b[n - 1] / A[n - 1][n - 1]
  
  for i in range(n - 1, -1, -1):
    sum = b[i]
    for j in range(i + 1, n):
      sum -= A[i][j] * x[j]
    x[i] = sum / A[i][i]
  print(x)
  return(x)

A = [[3, 2, -5], [2, -3, 1], [1, 4, -1]]
b = [2, 1, 4]

GE(A, b)
