# coding=utf-8

"""
返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。此处所说的对象应该特指复合类型的对象(如类、list等)，对于字符串、整数等类型，变量的id是随值的改变而改变的。
Python版本： Python2.x Python3.x
"""


class Obj():
    def __init__(self, arg):
        self.x = arg


if __name__ == '__main__':
    obj = Obj(1)
    print id(obj)  # 32754432
    obj.x = 2
    print id(obj)  # 32754432

    s = "abc"
    print id(s)  # 140190448953184
    s = "bcd"
    print id(s)  # 32809848

    x = 1
    print id(x)  # 15760488
    x = 2
    print id(x)  # 15760464
