# coding=utf-8
# 记录函数函数名和调用参数的装饰器

from functools import wraps


def log_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        param_str = ""
        for value in args:
            param_str += str(value) + " "
        for key, value in kwargs.items():
            param_str += "{0}={1} ".format(key, value)
        print(func.__name__, param_str)
        return result
    return wrapper

@log_it
def my_function(*args, **kwargs):
    pass


my_function(1, 2, name="me", age=30)
