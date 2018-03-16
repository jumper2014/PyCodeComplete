# coding=utf-8
# run via python 2.7

"""
bytearray([source [, encoding [, errors]]])返回一个byte数组。Bytearray类型是一个可变的序列，并且序列中的元素的取值范围为 [0 ,255]。

参数source:

如果source为整数，则返回一个长度为source的初始化数组；

如果source为字符串，则按照指定的encoding将字符串转换为字节序列；

如果source为可迭代类型，则元素必须为[0 ,255]中的整数；

如果source为与buffer接口一致的对象，则此对象也可以被用于初始化bytearray.。

版本：在python2.6后新引入，在python3中同样可以使用！
"""

a = bytearray(3)
print repr(a)
print repr(a[0])
print repr(a[1])
print repr(a[2])

a = bytearray('abc')
print repr(a)
print repr(a[0])
print repr(a[1])
print repr(a[2])


a = bytearray([1, 2, 3])
print repr(a)
print repr(a[0])
print repr(a[1])
print repr(a[2])


a = bytearray(buffer("abc"))
print repr(a)
print repr(a[0])
print repr(a[1])
print repr(a[2])
