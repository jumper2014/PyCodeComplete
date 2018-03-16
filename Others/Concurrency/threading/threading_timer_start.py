# coding=utf-8
# 这个类表示一个动作应该在一个特定的时间之后运行 — 也就是一个计时器。
# Timer是Thread的子类， 因此也可以使用函数创建自定义线程。
from threading import Timer


def fun():
    print "hello, world"

if __name__ == '__main__':
    t = Timer(5.0, fun)
    t.start() # 5秒后, "hello, world"将被打印