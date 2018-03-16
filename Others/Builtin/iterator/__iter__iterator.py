# coding=utf-8
"""
__iter__ 方法会返回一个迭代器iterator
迭代器是拥有next(__next__)方法的对象，调用next时会返回下一个值
"""


class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break