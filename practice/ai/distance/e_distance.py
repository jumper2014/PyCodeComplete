#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 欧氏距离

import numpy as np

if __name__ == '__main__':
    x = np.random.random(10)
    y = np.random.random(10)
    print(x)
    print(y)

    # 根据公式求解欧氏距离
    d1 = np.sqrt(np.sum(np.square(x - y)))
    print(d1)
