import random     # Allows us to generate random numbers.
import math       # Allows us to use eulers # and square root.

def f(x, y, z):     # Defines the function, recieves 3 variables.
  return(y * x ** 2 + y * z + math.exp(x))  # Returns the value.

def integrate(a, b, c, d, r, w, n):   
  # This function is going to estimate an indefinite triple
  # integral by using generating random numbers between the
  # ranges and summing up the values returned from the function.
  # This function takes in 7 variables:
  # a and b: range of x.
  # c and d: range of y.
  # r and w: range of z.
  # n number of iterations.
  sum = 0     # Initalize variable sum at 0
  region = (b - a) * (d - c) * (w - r)  # Calculates the region value.
  for i in range(n):    # For loop iterates for n times.
    g = random.uniform(a, b)  # Generates a random # between a and b.
    h = random.uniform(c, d)  # Generates a random # between c and d.
    j = random.uniform(w, r)  # Generates a random # between w and r.
    sum += f(g, h, j)   # Adds to sum the value returned from f().
  ans = (sum * region / n)    # Averages the product of the sum and region.
  print(ans)    # Prints ans (answer).
  return(ans)   # Returns the value of ans.
# Stores true solution from Maple in variable truSol.
truSol = 110.3343366    
 # Calls the integrate function with specific parameters.
ans = integrate(0, 2, 3, 6, -1, 1, 100000)
# Calculates Relative Error.
relError = abs((truSol - ans) / truSol)
# Prints the comparison between the relative error and error: O(1/sqrt(n)).
print(relError, " | ", 1 / math.sqrt(100000))
