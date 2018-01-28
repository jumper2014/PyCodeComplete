#!/usr/bin/env python
# coding=utf-8
# string转换成list,tuple,dict

#################################################
# 字符串转换成列表
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
# <type 'str'>
b = eval(a)
print(b)
# [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
print(type(b))
# <type 'list'>

#################################################
# 字符串转换成字典
a = "{1: 'a', 2: 'b'}"
print(type(a))
# <type 'str'>
b = eval(a)
print(b)
# {1: 'a', 2: 'b'}
print(type(b))
# <type 'dict'>

#################################################
# 字符串转换成元组
a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(a))
# <type 'str'>
b = eval(a)
print(b)
# ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))
print(type(b))
# <type 'tuple'>
