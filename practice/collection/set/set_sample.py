#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    nums = {1, 2, 3}
    nums.add(4)
    squares = {x*x for x in nums}
    print(nums)
    print(squares)
    # {1, 2, 3, 4}
    # {16, 1, 4, 9}