# coding=utf-8
# 对字典进行排序

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x是一个元组列表,用每个元组的第1个元素排序
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print(sorted_x)
assert sorted_x == [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]

# 下面是另一种方法
# sorted_x是一个元组列表,用每个元组的第2个元素排序
sorted_x = sorted(x.items(), key=lambda x: x[1])
print(sorted_x)
assert sorted_x == [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]