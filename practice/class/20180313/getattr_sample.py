#!/usr/bin/env python
# coding=utf-8
# 演示__getattribute__的数据保护功能


class Count(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current = None

    def __getattribute__(self, item):
        print(type(item), item)
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self, item)
        # or you can use ---return super().__getattribute__(item)


obj1 = Count(1, 10)
print(obj1.min)
print(obj1.max)
print(obj1.current)
