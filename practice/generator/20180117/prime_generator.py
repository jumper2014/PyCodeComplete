#!/usr/bin/env python
# coding=utf-8
# 使用生成器迭代素数序列

import math


# 判断一个数字是否是素数
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(num)+1), 2):
            if num % current == 0:
                return False
        return True
    return False


# 生成器函数，start从什么位置开始向上查找素数
def get_primes(start):
    while True:
        if is_prime(start):
            yield start
        start += 1


if __name__ == "__main__":
    i = 0
    count = 10  # 一共查找多少个素数

    # 用for循环来迭代生成器
    for p in get_primes(2):
        print(p)
        i += 1
        if i >= count:
            break
