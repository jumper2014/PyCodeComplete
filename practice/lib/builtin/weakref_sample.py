#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import gc
import weakref
import sys


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    ##############################
    # 强引用
    ##############################
    a = A(88)
    print(sys.getrefcount(a))  # 2
    d = dict()
    d['primary'] = a
    print(d['primary'])         # 88
    print(sys.getrefcount(a))   # 3

    del a
    gc.collect()            # 立即进行垃圾回收
    print(d['primary'])     # 88 依然存在

    ##############################
    # 弱引用
    ##############################
    a = A(88)
    print(sys.getrefcount(a))   # 2
    d = weakref.WeakValueDictionary()
    d['primary'] = a            # 这里是弱引用
    print(d['primary'])         # 88
    print(sys.getrefcount(a))   # 2

    del a
    gc.collect()            # 立即进行垃圾回收
    print(d['primary'])  # 已经不存在，抛出KeyError异常

