#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import numpy as np
import matplotlib
import scipy.stats
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

if __name__ == "__main__":
    # 期望0，标准差1，条数50
    mu, sigma, num_bins = 0, 1, 50
    # 1M个随机数
    x = mu + sigma * np.random.randn(1000000)

    # 正态分布的数据, 颜色的透明度0.5
    n, bins, patches = plt.hist(x, num_bins, density=True, facecolor='blue', alpha=0.5)

    # 拟合曲线
    y = scipy.stats.norm.pdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('histogram of normal distribution: $\mu = 0$, $\sigma=1$')

    plt.subplots_adjust(left=0.15)
    plt.show()
