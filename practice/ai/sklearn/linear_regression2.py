# Importing the libraries
import pandas as pd
import numpy
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 导入数据集合
df = pd.read_csv('../datasets/50_Startups.csv')
X = df.iloc[:, :-1].values  # 前4列
Y = df.iloc[:, 4].values  # profit

# 将类别数据数字化
label_encoder = LabelEncoder()
X[:, 3] = label_encoder.fit_transform(X[:, 3])
one_hot_encoder = OneHotEncoder(categorical_features=[3])
X = one_hot_encoder.fit_transform(X).toarray()
print(X)

# 躲避虚拟变量陷阱
X = X[:, 1:]

# 切分训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# 用线性回归模型进行训练
regression = LinearRegression()
regression.fit(X_train, Y_train)

# 预测测试集合的结果
Y_pred = regression.predict(X_test)

# 回归评价，模型越好：r2→1；模型越差：r2→0
print(r2_score(Y_test, Y_pred))

# arange(10),会生成数组([0,1,2,3,4,5,6,7,8,9])，作为X值，生成10组对比值
plt.scatter(numpy.arange(10), Y_test, color='red', label='Y_test')
plt.scatter(numpy.arange(10), Y_pred, color='blue', label='Y_pred')

# 这里的legend函数就是将设置的标签显示出来
plt.legend(loc=2)
plt.show()
