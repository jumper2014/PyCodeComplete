#!/usr/bin/env python
# coding=utf-8
# 让装饰器带参数，
# 和不带参数的示例相比在外层多了一层包装。

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


@delay(2)
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, 2)
