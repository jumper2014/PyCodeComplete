# coding=utf-8
# 列表的内容复制

a = [1, 2, 3]
b = a[:]
assert b == a and b is not a
