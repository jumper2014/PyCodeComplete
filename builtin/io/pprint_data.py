# coding=utf-8
# pprint 是 pretty printer 的缩写，用来打印 Python 数据结构，与 print 相比，它打印出来的结构更加整齐，便于阅读。

import pprint
data = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )

print data

pprint.pprint(data)