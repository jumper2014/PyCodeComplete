# coding=utf-8

from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print clf.coef_
# array([ 0.5,  0.5])