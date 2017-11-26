# coding=utf-8
"""
为了解决MyRange的问题，可以分别定义可迭代类型对象和迭代器类型对象；
然后可迭代类型对象的__iter__()方法可以获得一个迭代器类型的对象。
"""


class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZrangeIterator(self.n)


class ZrangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

zrange = Zrange(3)
print zrange is iter(zrange)

print [i for i in zrange]
print [i for i in zrange]