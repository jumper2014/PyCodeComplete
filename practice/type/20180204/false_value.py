#!/usr/bin/env python
# coding=utf-8


def print_boolean_value(value):
    if value:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    # 下面所有的结果都是False
    print_boolean_value(None)
    print_boolean_value(False)
    # 所有值为0的数
    print_boolean_value(0)
    print_boolean_value(0.0)
    print_boolean_value(0L)
    print_boolean_value(0.0 + 0.0j)
    print_boolean_value("")
    print_boolean_value([])
    print_boolean_value(())
    print_boolean_value({})