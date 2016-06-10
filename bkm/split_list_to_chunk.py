# coding=utf-8
# 把列表分隔成同样大小的块

import pprint
# xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。


def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i: i+n]


pprint.pprint(list(chunks(range(10, 75), 10)))

# 一句话
l = range(10, 75)
n = 10
print tuple(l[i: i+n] for i in xrange(0, len(l), n))