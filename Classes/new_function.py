# coding=utf-8
"""
继承自object的新式类才有__new__

先__new__(), 后__init()

__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，
__init__不需要返回值

"""


class MyClass(object):
    def __init__(self):
        print "init"

    def __new__(cls, *args, **kwargs):
        print "new %s" % cls
        return object.__new__(cls, *args, **kwargs)


MyClass()
