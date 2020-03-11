import math

def quad_roots(a, b, c):
  #a, b, and c are real numbers.
  #discrimnate:
  dis = b ** 2 - 4.0 * a * c
  #if a and b are equal to 0
  if a == 0 and b == 0: 
    #if c is equal to 0
    if c == 0:
      print("y = 0 everywhere")
      return
    else: #c/=0 no solution
      print("There is no solution.")
      return
  if a == 0:
    print("The solution is", -c / b)
    return
  if b == 0 and c == 0:
    print("There is one root at the origin: (0, 0).")
    return
  if dis < 0: #no real roots
    print("There is no real solution")
    return
  if b > 0:
    x = (-b - math.sqrt(dis))
    print("The roots are", x / (2 * a), ", ", (2 * c) / x)
  else:
    x = (-b + math.sqrt(dis))
    print("The roots are", x / (2 * a), ", ", (2 * c) / x)

quad_roots(0, 0, 0)
quad_roots(0, 0, 1)
quad_roots(0, 2, 14)
quad_roots(9, 0, 0)
quad_roots(1, 2, 1)
quad_roots(1, 2, 14)
quad_roots(1, 2, -15)
quad_roots(1, -2, -15)