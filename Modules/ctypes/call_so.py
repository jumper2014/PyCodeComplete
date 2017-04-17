# coding=utf-8
# call .so function within python

from ctypes import cdll

cur = cdll.LoadLibrary('./a.so')
cur.show()
print cur.add(1, 2)
