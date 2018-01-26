#!/usr/bin/env python
# coding=utf-8
# 演示使用闭包代替类


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


class Multiplier(object):
    def __init__(self, faciend):
        self.faciend = faciend

    def product(self, multiplicator):
        return self.faciend * multiplicator

if __name__ == "__main__":
    # 使用闭包
    # Multiplier of 3
    times3 = make_multiplier_of(3)

    # Multiplier of 5
    times5 = make_multiplier_of(5)

    # Output: 27
    print(times3(9))

    # Output: 15
    print(times5(3))

    # 使用类
    # Output: 27
    mul = Multiplier(3)
    print(mul.product(9))

    # Output: 15
    mul = Multiplier(5)
    print(mul.product(3))
