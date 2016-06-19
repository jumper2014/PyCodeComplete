# coding=utf-8
# 求最大最小元素

import random
import heapq

a = [random.randint(0, 100) for __ in xrange(100)]
print heapq.nsmallest(5, a)

print heapq.nlargest(5, a)
