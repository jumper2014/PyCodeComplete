# coding=utf-8
# 变化的函数默认参数

"""
python中的函数是最高等级的对象,而不仅仅是一小段代码
一个函数是一个被它自己定义而执行的对象,默认数据是一种成员数据,
所以它们的状态和其他对象一样,会随着每一次调用而改变
"""


def foo(a=[]):
    a.append(5)
    return a


print foo()
print foo()
print foo()

