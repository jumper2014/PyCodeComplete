# coding=utf-8


# 无参数装饰器 – 包装无参数函数
def decorator(func):
    print "hello"
    return func


@decorator
def foo():
    print "in foo"

foo()


# 无参数装饰器 – 包装带参数函数
def decorator_func_args(func):
    def handle_args(*args, **kwargs):
        print "begin"
        func(*args, **kwargs)
        print "end"
    return handle_args


@decorator_func_args
def foo2(a, b=2):
    print a, b

foo2(1)


# 内置的装饰器有三个：staticmethod,classmethod, property
class A():
    @staticmethod
    def test_static():
        print "static"

    def test_normal(self):
        print "normal"

    @classmethod
    def test_class(cls):
        print "class", cls

a = A()
A.test_static()
a.test_static()
a.test_normal()
a.test_class()
