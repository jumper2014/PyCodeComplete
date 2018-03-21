#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

@profile
def foo():
    result = 0
    for i in range(100000):
        result += i
    return result


if __name__ == '__main__':
    foo()