# coding=utf-8
# 用range生成list和generator

L = [x*x for x in range(10)]
print type(L)
print L

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

g = (x*x for x in range(10))
print type(g)
print g
print g.next()
print g.next()
print g.next()

# 不断调用next()方法实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
g = (x*x for x in range(10))
for i in g:
    print i
