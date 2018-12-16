#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 汉明距离


def hmd4str(s1, s2):
    """字符串的汉明距离"""
    if len(s1) != len(s2):
        raise ValueError("不等长")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


def hmd4int(x, y):
    """整数的汉明距离"""
    z = x ^ y
    count = 0
    while z != 0:
        if z & 1 == 1:
            count += 1
        z = z >> 1
    return count


if __name__ == '__main__':
    print(hmd4str("abcdefg", "abbdegg"))
    print(hmd4int(9, 15))