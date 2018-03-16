# coding=utf-8
# 记录函数执行时间的装饰器

import time
from functools import wraps


def time_this(func):
    """
    Decorator that report the execution time
    :param func: function
    :return: None
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@time_this
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000000)
