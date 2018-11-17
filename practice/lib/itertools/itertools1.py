#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import itertools

if __name__ == '__main__':
    x = itertools.chain(range(3), range(4), [3, 2, 1])
    print(list(x))
    # [0, 1, 2, 0, 1, 2, 3, 3, 2, 1]


    x = itertools.accumulate(range(10))
    print(list(x))
    # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

