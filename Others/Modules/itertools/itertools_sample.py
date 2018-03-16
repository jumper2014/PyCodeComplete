# coding=utf-8
# itertools中的函数大多是返回各种迭代器对象

import itertools

# itertools.chain 连接多个列表或者迭代器
x = itertools.chain(range(3), range(4), [3, 2, 1])
print (list(x))
# [0, 1, 2, 0, 1, 2, 3, 3, 2, 1]


# itertools.combinations
# 求列表或生成器中指定数目的元素不重复的所有组合
x = itertools.combinations(range(4), 3)
print(list(x))
# [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

# itertools.combinations_with_replacement
# 允许重复元素的组合
x = itertools.combinations_with_replacement('ABC', 2)
print(list(x))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# itertools.compress
# 按照真值表筛选元素
x = itertools.compress(range(5), (True, False, True, True, False))
print(list(x))
# [0, 2, 3]


# itertools.count
# 就是一个计数器,可以指定起始位置和步长
x = itertools.count(start=20, step=-1)
print(list(itertools.islice(x, 0, 10, 1)))
# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# itertools.cycle
# 循环指定的列表和迭代器
x = itertools.cycle('ABC')
print(list(itertools.islice(x, 0, 10, 1)))
# ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']


# itertools.dropwhile
# 按照真值函数丢弃掉列表和迭代器前面的元素
x = itertools.dropwhile(lambda e: e < 5, range(10))
print(list(x))
# [5, 6, 7, 8, 9]

# itertools.groupby
# 按照分组函数的值对元素进行分组
x = itertools.groupby(range(10), lambda x: x < 5 or x > 8)
for condition, numbers in x:
    print(condition, list(numbers))
# True [0, 1, 2, 3, 4]
# False [5, 6, 7, 8]
# True [9]

# itertools.islice
# 上文使用过的函数，对迭代器进行切片
x = itertools.islice(range(10), 0, 9, 2)
print(list(x))
# [0, 2, 4, 6, 8]


# itertools.permutations
# 产生指定数目的元素的所有排列(顺序有关)
x = itertools.permutations(range(4), 3)
print(list(x))

# itertools.product
# 产生多个列表和迭代器的(积)
x = itertools.product('ABC', range(3))
print(list(x))
# [('A', 0), ('A', 1), ('A', 2), ('B', 0), ('B', 1), ('B', 2), ('C', 0), ('C', 1), ('C', 2)]

# itertools.repeat
# 简单的生成一个拥有指定数目元素的迭代器
x = itertools.repeat(0, 5)
print(list(x))
# [0, 0, 0, 0, 0]

# itertools.takewhile
# 与dropwhile相反，保留元素直至真值函数值为假。
x = itertools.takewhile(lambda e: e < 5, range(10))
print(list(x))
# [0, 1, 2, 3, 4]

# itertools.starmap
# 类似map
x = itertools.starmap(str.islower, 'aBCDefGhI')
print(list(x))
# [True, False, False, False, True, True, False, True, False]
