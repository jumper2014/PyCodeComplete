# coding=utf-8
"""
myRange这个对象就是一个可迭代对象，同时它本身也是一个迭代器对象。
对于一个可迭代对象，如果它本身又是一个迭代器对象，就没有办法支持多次迭代。
"""


class MyRange(object):
    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()

myRange = MyRange(3)
print[i for i in myRange]
print[i for i in myRange]

# [0, 1, 2]
# []
