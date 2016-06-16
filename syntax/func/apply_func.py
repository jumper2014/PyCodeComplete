# coding=utf-8
# 展示如何使用apply函数

def func(x, y, z):
    return x + y + z

print apply(func, (2, 3, 4))

f = lambda x, y, z: x + y + z
print apply(f, (2, 3, 4))