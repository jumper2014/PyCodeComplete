# coding=utf-8
"""
__getattribute__, 当特性被访问时自动调用（只能在新式类中使用）


"""


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def __getattribute__(self, item):
        print "visit item: {0}".format(item)
        return object.__getattribute__(self, item)


rect = Rectangle()
print rect.width

