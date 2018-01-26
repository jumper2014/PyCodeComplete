#!/usr/bin/env python
# coding=utf-8

import time


def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        ret = func(*args, **kwargs)
        print("delay 1 second to call %s" % func.__name__)
        return ret
    return wrapper


@delay
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, 2)
