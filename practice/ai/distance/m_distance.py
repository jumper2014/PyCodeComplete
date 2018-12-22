#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 曼哈顿距离

import numpy as np

if __name__ == '__main__':
    x = np.random.random(10)
    y = np.random.random(10)
    print(x)
    print(y)

    # 根据公式求解曼哈顿距离
    d1 = np.sum(np.abs(x - y))
    print(d1)