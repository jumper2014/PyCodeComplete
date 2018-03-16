# coding=utf-8

#!/usr/bin/env python2.4
# This program shows off a python decorator(
# which implements tail call optimization. It
# does this by throwing an exception if it is
# it's own grandparent, and catching such
# exceptions to recall the stack.

import sys

class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated
    function recurses in a non-tail context.
    """
    def func(*args, **kwargs):
        f = sys._getframe()
        # 为什么是grandparent, 函数默认的第一层递归是父调用,
        # 对于尾递归, 不希望产生新的函数调用(即:祖父调用),
        # 所以这里抛出异常, 拿到参数, 退出被修饰函数的递归调用栈!(后面有动图分析)
        if f.f_back and f.f_back.f_back \
            and f.f_back.f_back.f_code == f.f_code:
            # 抛出异常
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    # 捕获异常, 拿到参数, 退出被修饰函数的递归调用栈
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def factorial(n, acc=1):
    "calculate a factorial"
    if n == 0:
        return acc
    return factorial(n-1, n*acc)

print(factorial(10000))
