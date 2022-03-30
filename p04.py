from matplotlib import pyplot
import numpy as np

def all_equal(list):
    return len(set(list)) <= 1

def makeLeafNode(gini, num_samples, class_counts):
	leaf = {
		'gini': gini, # the gini value for the samples in the node 
		'samples': num_samples, # the number of samples in the node
		'value': class_counts, # a list of the number of samples in each class
		'left': None, # the left child node
		'right': None # the right child node
	}
	return leaf

def makeNode(gini, num_samples, class_counts, feature, threshold, left, right):
	node = {
		'gini': gini, # the gini value for the samples in the node 
		'samples': num_samples, # the number of samples in the node
		'value': class_counts, # a list of the number of samples in each class
		'feature': feature, # the feature to split on
		'threshold': threshold, # threshold value.
		'left': left, # the left child node
		'right': right # the right child node
	}
	return node

def shouldSplit(x, y, n_classes, max_depth, min_samples_split):
	x0 = [x[i][0] for i in range(len(x))]
	x1 = [x[i][1] for i in range(len(x))]
	if max_depth == 0:
		return False
	elif len(x) < min_samples_split:
		return False
	elif all_equal(y):
		return False
	elif (all_equal(x0) and all_equal(x1)):
		return False
	else:
		return True

def getThresholds(x, f):
	xnew = []
	for i in range(len(x)):
		xnew.append(x[i][f])
	xnew = list(set(xnew))
	xnew.sort()
	result = []
	for i in range(len(xnew) - 1):
		t = (xnew[i] + xnew[i + 1]) / 2
		result.append(t)
	return result

def computeGini(value, n_classes):
	s = 0
	t = sum(value)
	for i in range(n_classes):
		if t == 0:
			continue
		s += (value[i] / t) ** 2
	return 1 - s

def computeGiniImp(value_left, value_right, Igl, Igr):
	n_l, n_r = sum(value_left), sum(value_right)
	return (n_l * Igl + n_r * Igr) / (n_l + n_r)

def getCurrentNode(y, n_classes):
	value = [0 for i in range(n_classes)]
	for i in y:
		value[i] += 1
	Ig = computeGini(value, n_classes)
	return value, Ig
	
def split(x, y, n_classes, f, t):
	value_left = [0 for i in range(n_classes)]
	value_right = [0 for i in range(n_classes)]
	x_left, x_right = [], []
	y_left, y_right = [], []
	for i in range(len(x)):
		temp = x[i][f]
		if temp <= t:
			value_left[y[i]] += 1
			x_left.append(x[i])
			y_left.append(y[i])
		else:
			value_right[y[i]] += 1
			x_right.append(x[i])
			y_right.append(y[i])
	return x_left, x_right, y_left, y_right, value_left, value_right

def best_split(x, y, n_classes):
	valueO, IgO = getCurrentNode(y, n_classes)
	Ig_new = 1
	M = len(x[0]) - 1
	for f in range(M, -1, -1):
		thresholds = getThresholds(x, f)
		for t in thresholds:
			x_left, x_right, y_left, y_right, value_left, value_right = split(x, y, n_classes, f, t)
			Igl = computeGini(value_left, n_classes)
			Igr = computeGini(value_right, n_classes)
			Ig = computeGiniImp(value_left, value_right, Igl, Igr)
			if Ig < Ig_new:
				Ig_new = Ig
				f_new = f
				t_new = t
	x_left, x_right, y_left, y_right, value_left, value_right = split(x, y, n_classes, f_new, t_new)
	return (valueO, IgO, x_left, x_right, y_left, y_right, value_left, 
			value_right, Ig_new, f_new, t_new)

def buildTree(x, y, n_classes, max_depth, min_samp):
	status = shouldSplit(x, y, n_classes, max_depth, min_samp)
	if status and max_depth != None:
		data = best_split(x, y, n_classes)
		node = makeNode(data[1], sum(data[0]), data[0], data[-2], data[-1], 
						buildTree(data[2], data[4], n_classes, max_depth - 1, min_samp), buildTree(data[3], data[5], n_classes, max_depth - 1, min_samp))
		return node
	elif status and max_depth == None:
		data = best_split(x, y, n_classes)
		node = makeNode(data[1], sum(data[0]), data[0], data[-2], data[-1], 
						buildTree(data[2], data[4], n_classes, max_depth, min_samp), buildTree(data[3], data[5], n_classes, max_depth, min_samp))
		return node
	else:
		value, gini = getCurrentNode(y, n_classes)
		leaf = makeLeafNode(gini, sum(value), value)
		return leaf
	
def decision_tree_fit(x, y, n_classes, max_depth, min_samples_split):
	tree = buildTree(x, y, n_classes, max_depth, min_samples_split)
	return tree

def classifySample(node, row):
	l = 'left'
	r = 'right'
	if not node[l] and not node[r]:
		value = node['value']
		m = max(value)
		return value.index(m)
	else:
		xjt = row[node['feature']]
		theta = node['threshold']
		if xjt <= theta:
			node = node['left']
			return classifySample(node, row)
		else:
			node = node['right']
			return classifySample(node, row)
	
def decision_tree_predict(dt, x):
	y_hat = []
	for i in range(len(x)):
		y_hat.append(classifySample(dt, x[i]))
	return y_hat


