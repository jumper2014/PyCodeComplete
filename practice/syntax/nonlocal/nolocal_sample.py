#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def count_down(n):
    def decrement():
        nonlocal n
        n -= 1

    while n > 0:
        print(n)
        decrement()


if __name__ == '__main__':
    count_down(3)
