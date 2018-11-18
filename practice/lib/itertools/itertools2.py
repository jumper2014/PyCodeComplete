#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import itertools

if __name__ == '__main__':
    x = itertools.compress(range(5), (True, False, True, True, False))
    print(list(x))
    # [0, 2, 3]

    x = itertools.combinations_with_replacement('ABC', 2)
    print(list(x))
    # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

    x = itertools.combinations(range(4), 3)
    print(list(x))
    # [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]