#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def bar():
    result = 0
    for i in range(1000000):
        result += i
    return result


def foo():
    result = 0
    for i in range(100000):
        result += i
    for i in range(5):
        bar()
    return result


if __name__ == '__main__':
    import cProfile

    # 直接把分析结果打印到控制台
    cProfile.run("foo()")

    # 根据cumtime列排序后打印到控制台，
    # 也就是说按包含子函数执行的时间顺序进行排序
    cProfile.run("foo()", sort="cumulative")

    # 把分析结果保存到文件中
    cProfile.run("foo()", filename="result.out")
