#!/usr/bin/env python

#============================================#
#
# Author: penn - penn201500@gmail.com
# Last modified: 2017-03-05 14:21
# Filename: test_yeild.py
# Description:
#
#===========================================#

def test_yeild():
    for i in range(1,10):
        yield i

if __name__ == '__main__':
    for i in test_yeild():
        print i
