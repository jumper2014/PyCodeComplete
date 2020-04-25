#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 求多个数的最大公约数
# math 模块有个求两个数最大公约数的函数gcd
# reduce在Python2是内置函数，Python3中迁移到functools模块中

import math
import functools

if __name__ == '__main__':
    num_list = [30, 40, 60, 15]

    gcd_result = functools.reduce(math.gcd, num_list)
    print(gcd_result)
