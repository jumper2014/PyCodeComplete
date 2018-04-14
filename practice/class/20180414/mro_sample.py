#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 多重继承中的MRO顺序


class A():
    def who_am_i(self):
        print("I am A")


class B(A):
    pass


class C(A):
    def who_am_i(self):
        print("I am C")


class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
    d.who_am_i()    # I am C

    print(D.__mro__)
    # (<class '__main__.D'>, < class '__main__.B' >, < class '__main__.C' >, < class '__main__.A' >, < class 'object' > )
