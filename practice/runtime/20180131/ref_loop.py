#!/usr/bin/env python
# coding=utf-8
# 演示循环引用

import objgraph  # 可以用来检测内存泄漏

if __name__ == '__main__':
    a = list()
    b = list()
    # 查看list类型对象的数量
    # output: n
    print(objgraph.count('list'))
    a.append(b)
    # b.append(a)  # 循环引用

    print(a)
    print(b)
    del a
    del b
    # 再次查看list类型对象的数量
    # output: n
    print(objgraph.count('list'))
