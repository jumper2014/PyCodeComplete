# coding=utf-8
"""
静态方法是一种普通函数，就位于类定义的命名空间中，它不会对任何实例类型进行操作。
使用装饰器@staticmethod定义静态方法。
类对象和实例都可以调用静态方法
"""


class MyClass(object):
    @staticmethod
    def get_max_value():
        return 100

print MyClass.get_max_value()
