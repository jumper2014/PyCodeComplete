# coding=utf-8
"""
类方法是将类本身作为对象进行操作的方法。类方法使用@classmethod装饰器定义，
其第一个参数是类，约定写为cls。类对象和实例都可以调用类方法
"""


class MyClass(object):
    @classmethod
    def get_max_value(cls):
        return 100

print MyClass.get_max_value()
cl = MyClass()
print cl.get_max_value()

