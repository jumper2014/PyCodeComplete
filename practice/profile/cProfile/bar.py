#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def bar():
    result = 0
    for i in range(1000000):
        result += i
    return result
