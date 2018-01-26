#!/usr/bin/env python
# coding=utf-8
# 创建一个迭代成年用户的迭代器
# for Python 2.7


class AdultIterable(object):
    def __init__(self, ages):
        self.__ages = ages

    def __iter__(self):
        print("call iterable __iter__()")
        return AdultIterator([x for x in self.__ages if x >= 18])


class AdultIterator(object):
    def __init__(self, data):
        self.__data = data
        self.__index = 0

    def __iter__(self):
        return self

    def next(self):
        print("call iterator next()")
        if self.__index < len(self.__data):
            val = self.__data[self.__index]
            self.__index += 1
            return val
        else:
            raise StopIteration


if __name__ == "__main__":
    user_ages = list(range(12, 60))
    ages = AdultIterable(user_ages)  # 生成一个可迭代对象

    age = iter(ages)    # 生成一个迭代器
    print(next(age))   # 用迭代器来遍历可迭代对象
    print(next(age))   # 用迭代器来遍历可迭代对象

    for age in ages:    # 用for来遍历
        print age
