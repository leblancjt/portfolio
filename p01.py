def dot_product(u, v):
	l1 = len(u)
	l2 = len(v)
	if l1 == l2:
		sum = 0
		for i in range(l1):
			sum += u[i] * v[i]
		return sum
	else:
		print("Vectors given are not the same length.")

def matrix_multiply(a, b):
	r = len(b)
	c = len(a[0])
	if r == c:
		r = len(a)
		c = len(b[0])
		result = []
		for i in range(r):
			result.append([])
			for j in range(c):
				result[i].append(0)
		for i in range(len(a)):
			for j in range(len(b[0])):
				for k in range(len(b)):
					result[i][j] += a[i][k] * b[k][j]
		return result
	else:
		print("Matrices given do not have compatible dimensions")
	
def slr_cost(x, y, w_0, w_1):
	n = len(x)
	sum = 0
	for i in range(n):
		sum += (y[i] - w_0 - (w_1 * x[i])) ** 2
	return (1 / (2 * float(n))) * sum


def slr_gradient(x, y, w_0, w_1):
	n = len(x)
	g1 = 0
	g2 = 0
	for i in range(n):
		g1 += (y[i] - w_0 - w_1 * x[i]) * (-1)
		g2 += (y[i] - w_0 - w_1 * x[i]) * (-x[i])
	return ((g1 / float(n)), (g2 / float(n)))


def slr_analytical(x, y):
	m = len(x)
	t1 = 0
	t2 = 0
	xhat = 0
	yhat = 0
	for i in range(m):
		xhat += x[i]
		yhat += y[i]
	xhat = xhat / m
	yhat = yhat / m
	for i in range(m):
		t1 += (x[i] - xhat) * (y[i] - yhat)
		t2 += (x[i] - xhat) ** 2
	w1 = t1 / t2
	w0 = yhat - (w1 * xhat)
	return (w0, w1)

def slr_gradient_descent(x, y, w_0_init, w_1_init, eta, n_iter):
	w0 = w_0_init
	w1 = w_1_init
	for i in range(1, n_iter):
		print(slr_cost(x, y, w0, w1))
		w0 -= (eta * slr_gradient(x, y, w0, w1)[0])
		w1 -= (eta * slr_gradient(x, y, w0, w1)[1])
	return (w0, w1)

w0_init, w1_init = 0, 0
eta = 0.03
n_iter = 10
x = [8, 8, 4, 3, 6, 9, 8, 8, 3, 1]
y = [3.90, 3.87, 3.10, 2.95, 3.64, 4.26, 4.04, 4.04, 2.57, 2.15]
print(slr_gradient_descent(x, y, w0_init, w1_init, eta, n_iter))




