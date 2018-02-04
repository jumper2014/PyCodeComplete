#!/usr/bin/env python
# coding=utf-8


def print_boolean_value(value):
    if value:
        print('True')
    else:
        print('False')


class A(object):
    def __nonzero__(self):
        return False


class B(object):
    def __len__(self):
        return 0


class C(object):
    def __nonzero__(self):
        return False

    def __len__(self):
        return 1


class D(object):
    pass


if __name__ == '__main__':
    # 下面的结果是False
    print_boolean_value(A())
    print_boolean_value(B())
    print_boolean_value(C())
    # 下面的结果是True
    print_boolean_value(D())