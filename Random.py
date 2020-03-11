import random
import math

def rand(n):
  count = 0
  x = 0
  for i in range(n):
    xnew = random.random()
    if xnew > x:
      x = xnew
      count += 1
    else:
      x = xnew
  percent = (count / n) * 100
  print("Percent: ", percent, "%")

def mers(s, n):
# This program calculates Mersenne primes
# between 0 and 1
# Test randomness of the values by calculating the 
# the percentage of numbers greater than the previous
# n = number of primes needed
# s = seed
  k = 16807            #7^5
  j = 2147483647       #2^31-1
  x = 0                #intialize x
  count = 0            #count larger numbers

  for i in range(n):   #Repeat n times
    s = k * s % j
    xnew = s / j
    if xnew > x:       #If the new value is greater
      x = xnew         #Sets x to the value of the new value
      count += 1       #Add 1 to the count of larger numbers
    else:
      x = xnew
  percent = (count / n) * 100  #Calculates % of larger numbers
  print("Percent: ", percent, "%")

rand(10000)
mers(2, 10000)

def loaded(n):
  count = []
  count.append(0)
  count.append(0)
  count.append(0)
  count.append(0)
  count.append(0)
  count.append(0)

  for i in range(n):
    x = random.random()
    if x < 0.15:
      count[0] += 1
    elif x < 0.35:
      count[1] += 1
    elif x < 0.60:
      count[2] += 1
    elif x < 0.75:
      count[3] += 1
    elif x < 0.85:
      count[4] += 1
    elif x < 1:
      count[5] += 1
  percent = []
  percent.append((count[0] / n) * 100)
  percent.append((count[1] / n) * 100)
  percent.append((count[2] / n) * 100)
  percent.append((count[3] / n) * 100)
  percent.append((count[4] / n) * 100)
  percent.append((count[5] / n) * 100)
  print(percent)

loaded(1500)

def drunk(n):
  count = []
  count.append(0)  # x coordinate
  count.append(0)  # y coordinate
  outsideOf20 = 0 
  for i in range(n):
    for i in range (50):
      x = random.random()
      if x < (1/6):
        count[0] += 1
      elif x < ((1/6) + (1/4)):
        count[1] += 1
      elif x < ((1/6) + (1/2)):
        count[1] -= 1
      elif x < 1:
        count[0] -= 1
      dis = math.sqrt(count[0] ** 2 + count[1] ** 2)
      if dis <= 20:
        outsideOf20 += 1
    print(outsideOf20)
  print((outsideOf20 / n) * 100, "%")
    
drunk(100)
