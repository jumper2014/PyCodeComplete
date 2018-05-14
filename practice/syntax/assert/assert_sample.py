#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def divide(num1, num2):
    assert num2 != 0, "Divisor cannot be zero"
    return num1 / num2


if __name__ == '__main__':
    try:
        a2 = divide(12, 0)
    except AssertionError as e:
        print(e)
    # Divisor cannot be zero
