# coding=utf-8
"""
__getattr__ 当特性被访问，且对象没有对应的特性时被自动调用
__setattr__ 当试图给特性赋值的时候被自动调用


"""


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def __getattr__(self, item):
        print "visit item: {0}".format(item)
        if item == "size":
            return self.width, self.height
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        print "set item: {0}".format(value)
        if key == "size":
            self.width, self.height = value
        else:
            self.__dict__[key] = value