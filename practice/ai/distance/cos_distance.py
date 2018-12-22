#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import numpy as np

if __name__ == '__main__':
    x = np.random.random(10)
    y = np.random.random(10)
    print(x)
    print(y)

    # 根据公式求解
    # np.dot 点积
    # np.linalog.norm 向量的2范数, 即向量的每个元素的平方和再开平方根，
    d1 = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
    print(d1)