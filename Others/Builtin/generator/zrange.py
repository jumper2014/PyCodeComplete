# coding=utf-8
"""
在Python中，使用生成器可以很方便的支持迭代器协议。
生成器通过生成器函数产生，生成器函数可以通过常规的def语句来定义，
但是不用return返回，而是用yield一次返回一个结果，
在每个结果之间挂起和继续它们的状态，来自动实现迭代协议。
"""


def Zrange(n):
    print "begining of Zrange"
    i = 0
    while i < n:
        print "before yield", i
        yield i
        i += 1
        print "after yield", i
    print "endding fo Zrange"


zrange = Zrange(3)
print "---------"

print zrange.next()
print "---------"

print zrange.next()
print "---------"

print zrange.next()
print "---------"
