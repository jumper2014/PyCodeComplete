# coding=utf-8

# 可以通过以下方式访问类变量


class Foo(object):

    val = 3

    def __init__(self):
        print self.__class__.val


if __name__ == '__main__':
    foo = Foo()