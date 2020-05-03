#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

# 这段代码用来演示Python中的无穷大和NaN
# NaN 代表 not a number
import math

if __name__ == '__main__':
    # Python通过float创建正无穷大和负无穷大
    a = float("inf")
    b = float("-inf")

    # 使用math.isinf()来验证无穷大
    print(math.isinf(a)) # True
    print(math.isinf(b)) # True

    # 无穷大运算
    print(100+a)  # inf
    print(100+b)  # -inf
    print(100/a)  # 0.0

    # 正负无穷大相加是NaN
    print(a+b)  # nan

    # NaN运算
    c = float("nan")
    print(100+c)  # nan
    print(100/c)  # nan
    print(100*c)  # nan
    # 判断NaN
    print(math.isnan(c))  # True

    # nan值的任何比较操作都返回False
    print(c == c)   # False
    print(c > 100)  # False
    print(c <= 100)  # False


