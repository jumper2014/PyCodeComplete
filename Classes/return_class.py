# coding=utf-8
__author__ = 'zengyuetian'


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('foo')
print MyClass
