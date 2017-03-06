#!/usr/bin/env python

#============================================#
#
# Author: penn - penn201500@gmail.com
# Last modified: 2017-03-05 14:23
# Filename: test_yield_from.py
# Description:
2
#===========================================#

def test_yield():
    for i in range(1,8):
        yield i

def generator2():
    for i in range(10):
        yield i

def generator3():
    for j in range(10, 20):
        yield j

def generator():
    for i in generator2():
        yield i
    for j in generator3():
        yield j

if __name__ == '__main__':
    for k in generator():
		print k
