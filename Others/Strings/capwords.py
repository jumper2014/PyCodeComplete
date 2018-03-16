#!/usr/bin/env python
# coding=utf-8
import string

s = 'this quick brown fox jumped over the lazy dog'
print s
print string.capwords(s)
# This Quick Brown Fox Jumped Over The Lazy Dog
# capwords是先split(),然后capitalize(),最后join()而成。
# string.capwords(s[, sep])
# 该方法也可以将多个空格压缩成一个空格，并且删掉尾部的空格
s1 = 'test    several whitespace, and trailing whitespace    '
print s1
print string.capwords(s1)
#Test Several Whitespace, And Trailing Whitespace
