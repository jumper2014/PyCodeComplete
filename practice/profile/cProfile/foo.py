#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from bar import bar


def foo():
    result = 0
    for i in range(100000):
        result += i
    for i in range(5):
        bar()
    return result


if __name__ == '__main__':
    foo()
