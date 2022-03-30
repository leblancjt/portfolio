import sklearn
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from matplotlib import pyplot
import pandas as pd
import numpy

def news_control_1():
	pipe = Pipeline([('vect', CountVectorizer()),
					('scale', StandardScaler())])
	param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
	param_grid = [{'vect__C:' : param_range,
				   'vect__kernel' : ['linear']},
				  {'vect__C' : param_range,
				  'vect__gamma' : param_range,
				  'vect__kernel' : ['rbf']}]
	gs = GridSearchCV(estimator = pipe, param_grid = param_grid, scoring = 'accuracy', refit = True, cv = 10, n_jobs = -1)
	return gs
	
	
	
	
	

from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold # load data
df_train = pd.read_csv('news_control_1_train.csv')
x_train = df_train['text']
y_train = df_train['control_1'] # train the classifier
estimator = news_control_1().fit(x_train, y_train) # predict labels
 
y_hat_train = estimator.predict(x_train)
acc_train = balanced_accuracy_score(y_train, y_hat_train)
print(f'train accuracy: {acc_train:.3f}')
cv = StratifiedKFold(n_splits=3)
acc_cv = cross_val_score(estimator, x_train, y_train, cv=cv, scoring='balanced_accuracy', verbose=True)
print(f'cross validation accuracy: {acc_cv.mean():.3f} 'f'+/- {acc_cv.std():.3f}')
