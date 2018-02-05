#!/usr/bin/env python
# coding=utf-8
#  __bool__优先级比 __len__ 高
# 需要Python 3


class MyClass(object):
    def __init__(self):
        pass

    def __bool__(self):
        return False

    def __len__(self):
        return 1


def print_boolean_value(value):
    if value:
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    obj = MyClass()
    # output: False
    print_boolean_value(obj)

