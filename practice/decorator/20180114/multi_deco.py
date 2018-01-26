#!/usr/bin/env python
# coding=utf-8
# 多层装饰器

import time


def delay(sec):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            time.sleep(sec)
            ret = func(*args, **kwargs)
            print("delay %d seconds to call %s" % (sec, func.__name__))
            return ret
        return _wrapper
    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        cost = time.time() - start
        print("cost %f second " % cost)
        return ret
    return wrapper


@timeit
@delay(2)
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, 2)
