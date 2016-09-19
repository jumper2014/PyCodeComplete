# coding=utf-8
"""
静态方法没有self参数，能够被类本身直接调用

__author__ = 'zengyuetian'

"""


class MyClass(object):
    @staticmethod
    def get_max_value():
        return 100

print MyClass.get_max_value()
