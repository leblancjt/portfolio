n = 4
r = 1.19

a = [2.2, 1.0, -1.0, 4.1, -6]
b = []

for k in range(-1, n):
  for j in range(n - 1, k, -1):
    b.append(round(r * a[j + 1], 3))
    a[j] += round(r * a[j + 1], 3)

a.reverse()
print(b[:n])
print(a[n])

def step_calc():
  dt = 0.0
  dx = 0.0
  for i in range(1, 100001):
    dt += 1.0 / 10.0
    dx = i / 10.0
  print('\n' + 'dt = ' + str(dt) + ', dx = ' + str(dx))

step_calc()