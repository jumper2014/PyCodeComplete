# coding=utf-8
# 求字典的交并差集合

d1 = dict(a=1, b=2)
d2 = dict(b=2, c=3)

v1 = d1.viewitems()
v2 = d2.viewitems()


set1 = v1 & v2     # 交集
print set1

dict3 = dict(set1)  # 可以转化为字典
print dict3

set1 = v1 | v2  # 并集
print set1

set1 = v1 - v2  # 差集(仅v1有,v2没有的)
print set1

set1 = v1 ^ v2  # 对称差集 (不会同时出现在 v1 和 v2 中)
print set1

