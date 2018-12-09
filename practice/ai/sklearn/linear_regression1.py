#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 线性回归预测

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 读取到data frame
df = pd.read_csv('../datasets/studentscores.csv')
X = df.iloc[:, : 1].values  # 第一列的所有行
Y = df.iloc[:, 1].values  # 第二列的所有行

# 拆分训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1 / 4, random_state=0)

# 用简单线性回归模型拟合训练集
regression = LinearRegression()
regression = regression.fit(X_train, Y_train)

# 预测结果
Y_pred = regression.predict(X_test)

# 可视化训练集预测结果
plt.scatter(X_train, Y_train, color='red')  # 散点图
plt.plot(X_train, regression.predict(X_train), color='blue')

# 可视化测试集预测结果
plt.scatter(X_test, Y_test, color='yellow')
plt.plot(X_test, Y_pred, color='black')
plt.show()
