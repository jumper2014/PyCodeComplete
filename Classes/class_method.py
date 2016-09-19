# coding=utf-8
"""
类方法在定义时需要有名为cls的参数，类方法可以直接用类的具体对象调用

__author__ = 'zengyuetian'

"""


class MyClass(object):
    @classmethod
    def get_max_value(cls):
        return 100

print MyClass.get_max_value()
cl = MyClass()
print cl.get_max_value()

