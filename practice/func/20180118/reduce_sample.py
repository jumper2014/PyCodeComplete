#!/usr/bin/env python
# coding=utf-8
# 使用reduce计算序列和与积


if __name__ == "__main__":
    # 计算和
    sum_result = reduce(lambda x, y: x+y, range(1, 10))
    assert(sum_result == 45)
    print(sum_result)

    # 计算阶乘
    factorial_result = reduce(lambda x, y: x * y, range(1, 10))
    assert(factorial_result == 362880)
    print(factorial_result)