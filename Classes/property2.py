# coding=utf-8
"""
property函数创建了一个属性，其中的访问器函数被当做参数（先取值，后赋值）


"""


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def get_size(self):
        return self.width, self.height

    def set_size(self, size):
        self.width, self.height = size

    # property函数创建了一个属性，其中的访问器函数被当做参数（先取值，后赋值）
    size = property(get_size, set_size)

r = Rectangle()
r.size = (10, 20)
print r.size
