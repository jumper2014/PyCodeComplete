#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import time
from functools import wraps
import random


def fn_timer(func):
    @wraps(func)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (func.func_name, str(t1 - t0))
               )
        return result

    return function_timer


@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])


if __name__ == "__main__":
    random_sort(2000000)
    # Total time running random_sort: 1.60562682152 seconds
