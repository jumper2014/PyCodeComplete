# coding=utf-8
# 访问集合中元素的个数

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print '%s : %d' % (letter, c[letter])
