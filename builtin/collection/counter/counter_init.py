# coding=utf-8
# 初始化Counter对象

import collections

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)

c = collections.Counter()
print 'Initial :', c

c.update('abcdaab')  # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
print 'Sequence:', c

c.update({'a':1, 'd':5})  # 增加
print 'Dict    :', c  # Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})