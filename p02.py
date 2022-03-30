# Author: John LeBlanc
# Date: 10/06/2020

import math

def net_input(x, w):
	r = len(x)
	c = len(x[0])
	result = []
	rows = []
	for i in range(r):
		newRow = []
		for j in range(len(w)):
			s = x[i][j] * w[j]
			newRow.append(s)
		rows.append(newRow)
	for k in rows:
		result.append(sum(k))
	return result

def sigmoid(z):
	result = []
	l = len(z)
	for i in range(l):
		newz = 1 / (1 + math.exp(-(z[i])))
		result.append(newz)
	return result

def logr_predict_proba(x, w):
	z = net_input(x, w)
	result = sigmoid(z)
	return result
	
def logr_predict(x, w):
	yhat = logr_predict_proba(x, w)
	result = []
	for y in yhat:
		if y >= 0.5:
			result.append(1)
		else:
			result.append(0)
	return result

def logr_cost(x, y, w):
	n = len(x)
	h = logr_predict_proba(x, w)
	s = []
	for i in range(n):
		s.append(y[i] * math.log(h[i]) + (1 - y[i]) * (math.log(1 - h[i])))
	s = sum(s)
	result = - 1 / n * s
	return result

def logr_gradient(x, y, w):
	n = len(x)
	h = logr_predict_proba(x, w)
	s = []
	for i in range(3):
		for j in range(len(x[0])):
			s.append((y[i] - h[i]) * (-x[i][j]))
	s = (1 / n) * sum(s)
	result = s
	return result

x = [[7, 4, 8], [0, 0, 2], [7, 7, 4], [3, 0, 8]]
y = [0, 1, 0, 1]
w = [-1, -2, 1]
print(logr_gradient(x, y, w))




