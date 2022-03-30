from matplotlib import pyplot 
import numpy as np

def net_input_numpy(x, w, w0):
	return np.array(w0 + np.dot(x, w))

def svm_w0_gradient(x, y, w, w0, lambda_):
	return(-np.sum(y * lambda_))

def svm_w_gradient(x, y, w, w0, lambda_):
	sum = 0
	for i in range(len(x)):
		sum += lambda_[i] * y[i] * x[i]
	result = w - sum
	return result

def svm_lambda_gradient(x, y, w, w0, lambda_):
	z = net_input_numpy(x, w, w0)
	result = -(y * z - 1)
	return result

def svm_active_lambda_gradient(lambda_, lambda_gradient, c):
	result = []
	for i in range(len(lambda_)):
		li = lambda_[i]
		lgi = lambda_gradient[i]
		r = 0
		if li == 0 and lgi < 0 or li == c and lgi > 0:
			r = li
		elif lgi <= (c - li):
			if lgi >= -li:
				r = lgi
			else:
				r = -li
		elif lgi > (c - li):
			r = c - li
		result.append(r)
	return np.array(result)
		

def svm_support_vectors(lambda_, c):
	result = []
	for l in lambda_:
		if l == 0:
			result.append(False)
		else:
			result.append(True)
	return result	
		
def svm_on_correct_hyperplane(lambda_, c):
	result = []
	for l in lambda_:
		if l == 0:
			result.append(False)
		elif l == c:
			result.append(False)
		else:
			result.append(True)
	return result

def svm_ksi(x, y, w, w0):
	z = net_input_numpy(x, w, w0)
	k = 1 - y * z
	result = []
	for i in range(len(k)):
		l = max(0, k[i])
		result.append(l)
	return result

def svm_misclassified(ksi):
	result = []
	for k in ksi:
		if k < 0 or k > 1.:
			result.append(True)
		else:
			result.append(False)
	return result

def svm_optimization(x, y, c, eta, n_iter):
	w = np.zeros(len(x[0]))
	w0 = 0
	lambda_ = np.zeros(len(x))
	
	for i in range(n_iter):
		deltaW0 = svm_w0_gradient(x, y, w, w0, lambda_)
		deltaW = svm_w_gradient(x, y, w, w0, lambda_)
		deltal = svm_lambda_gradient(x, y, w, w0, lambda_)
		ksi = svm_ksi(x, y, deltaW, deltaW0)
		miss = svm_misclassified(ksi)
		maxdwj = max(abs(deltaW))
		g = svm_active_lambda_gradient(lambda_, deltal, c)
		maxdl = max(abs(g))
		print('max(dL/dwj| = ' + str(maxdwj) + ', max(|dL/d lambda|) = ' + str(maxdl))
		for i in range(len(miss)):
			if miss[i] == False:
				w += eta * (y[i] * x[i] - 2 * (1 / n_iter) * w)
			else:
				w += eta * (-2 * (1 / n_iter) * w)
		w0 += eta * deltaW0
		lambda_ += eta * deltal
		t = []
		for l in lambda_:
			if l >= 0 and l <= c:
				t.append(l)
			else:
				t.append(0)
		lambda_ = t
		
	return w, w0, lambda_

def svm_plot(x, y, c, w, w0, lambda_):
	"""
	Uses the gradient of the primal Lagrangian function for Support Vector Machines to estimate the weights, bias, and Lagrangian multipliers.
	:param x: data matrix (n x m)
	:param y: target vector {-1, 1} (length n)
	:param c: SVM 'C' parameter
	:param w: weight vector (length m)
	:param w0: bias (scalar)
	:param lambda_: Lagrangian multiplier vector (length n) :return:
	"""
	fig, ax = plt.subplots()
	index = y == 1
	ax.scatter(x[index, 0], x[index, 1], marker = '+', c = 'tab:orange', edgecolors ='black',label = 'positive')
	index = y == -1
	ax.scatter(x[index, 0], x[index, 1], marker = 'o', c = 'blue', edgecolors = 'black', label = 'negative')
	index = svm_support_vectors(lambda_, c)
	ax.scatter(x[index, 0], x[index, 1], marker = 's', c = 'none', s = 100, edgecolors = 'black', label = 'support vectors')
	index = svm_on_correct_hyperplane(lambda_, c)
	ax.scatter(x[index, 0], x[index, 1], marker = 'o', c = 'none', s = 100, edgecolors = 'black', label = 'on correct hyperplane')
	index = svm_misclassified(svm_ksi(x, y, w, w0))
	ax.scatter(x[index, 0], x[index, 1], marker = 'd', c = 'none', s = 100, edgecolors = 'black', label = 'misclassified')
	xx1, xx2 = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
	zz1 = w0 + w[0] * xx1 + w[1] * xx2
	ax.contour(xx1, xx2, zz1, levels = [-1, 0, 1], linestyles=['dotted', 'dashed', 'dotted'], colors='black')
	ax.set_xlabel('x_1')
	ax.set_ylabel('x_2')
	fig.set_title(f'C = {c}')
	fig.legend()
	plt.show()
