#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import random
import timeit


def random_sort():
    return sorted([random.random() for i in range(2000000)])


if __name__ == "__main__":
    # 相当于命令行下的
    # python -m timeit -n 1 -s "import random; sorted([random.random() for i in range(2000000)])"
    t1 = timeit.timeit(stmt=random_sort, number=1)
    print(t1)

    # 相当于命令行下的
    # python -m timeit -n 2 -r 2 -s "import random; sorted([random.random() for i in range(2000000)])"
    t2 = timeit.repeat(stmt=random_sort, number=2, repeat=2)
    print(t2)
