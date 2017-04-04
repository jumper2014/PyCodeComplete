# coding=utf-8

__author__ = 'zengyuetian'

"""
检查对象object是否可调用。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
注意：类是可调用的，而类的实例实现了__call__()方法才可调用。
版本：该函数在python2.x版本中都可用。但是在python3.0版本中被移除，而在python3.2以后版本中被重新添加。
"""

print callable(0)

print callable("mystring")


def add(a, b):
    return a+b

print callable(add)


class A(object):
    def method(self):
        return 0

print callable(A)

a = A()
print callable(a)


class B(object):
    def __call__(self, *args, **kwargs):
        return 0

print callable(B)
b = B()
print callable(b)