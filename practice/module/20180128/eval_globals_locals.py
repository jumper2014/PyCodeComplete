#!/usr/bin/env python
# coding=utf-8


# 全局名称空间
x = 5
y = 6
z = 7
res0 = eval('x+y')
# output: 11
print(res0)


def foo():
    x = 1
    y = 2

    # 局部名称空间
    res1 = eval('x+y')
    # output: 3
    print(res1)

    # 全局名称空间
    res2 = eval('x+y', globals())
    # output: 11
    print(res2)

    # 优先使用局部名称空间
    res3 = eval('x+y', globals(), locals())
    # output: 13
    print(res3)

    # 优先使用局部名称空间
    res3 = eval('x+y', globals(), locals())
    # output: 13
    print(res3)

    # 混杂使用名称空间
    res4 = eval('x+z', globals(), locals())
    # output: 8
    print(res4)


foo()
