#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":
    # 加载iris数据集
    iris = datasets.load_iris()

    # 导入数据和标签
    iris_x = iris.data
    iris_y = iris.target
    print("data:", iris_x)
    print("target:", iris_y)

    # 划分为训练集和测试集数据
    x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)

    # 设置knn分类器
    knn = KNeighborsClassifier()

    # 进行训练
    knn.fit(x_train, y_train)

    # 使用训练好的knn进行数据预测
    print(knn.predict(x_test))
    print(y_test)
