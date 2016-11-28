# coding=utf-8

a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"

b = eval(a)
print b
print type(b)

a = "{1: 'a', 2: 'b'}"
b = eval(a)
print b
print type(b)

a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
b = eval(a)
print b
print type(b)
