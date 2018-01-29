#!/usr/bin/env python
# coding=utf-8
# 展示全局名称空间和局部名称空间


def foo():
    num = 10
    # 在局部名称空间中访问全局名称空间的变量
    # output: ('foo globals-num', 5)
    print("foo globals-num", globals()['num'])

    # output: ('foo locals-num', 10)
    print("foo locals-num", locals()['num'])


num = 5
foo()

# 在全局名称空间下，globals()和locals()返回相同的字典。
print("globals", globals())
print("locals", globals())
