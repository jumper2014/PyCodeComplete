# coding=utf-8
"""
在Python中，函数也是一种对象。实际上，任何一个有__call__()特殊方法的对象都被当作是函数。
"""


class SampleMore(object):
    def __call__(self, a):
        return a+10


add = SampleMore()
print(add(2))
print map(add, [2, 4, 6])
