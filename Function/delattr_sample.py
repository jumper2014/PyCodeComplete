# coding=utf-8
__author__ = 'zengyuetian'

"""
删除object对象名为name的属性。这个函数的命名真是简单易懂啊，和jquery里面差不多，但是功能不一样哦，注意一下。
参数object：对象。
参数name：属性名称字符串。
版本：各版本中都支持该函数，python3中仍可用。
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


tom = Person("Tom", 35)
print dir(tom)

delattr(tom, 'name')
print dir(tom)
