#!/usr/bin/env python
# coding=utf-8


class Count(object):
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax
        self.current = None

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self, item)
        # or you can use ---return super().__getattribute__(item)
        # note this class subclass object


obj1 = Count(1, 10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.current)
