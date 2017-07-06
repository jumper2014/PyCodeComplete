# coding=utf-8
# 循环访问序列中的元素和索引
# 用enumerate包装一个可迭代对象，可以同时使用迭代项和索引，在迭代的同时获取迭代项所在位置时非常方便。

# enumerate 还可以接收一个可选参数start，默认start等于0。
# enumerate(list, start=1)，这样index的起始值就是1

a = ['a', 'b', 'c', 'd', 'e']
for index, item in enumerate(a):
    print(index, item)

print("--------")

a = ['a', 'b', 'c', 'd', 'e']
for index, item in enumerate(a, 1):
    print(index, item)