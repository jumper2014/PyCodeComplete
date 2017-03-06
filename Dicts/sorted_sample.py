# coding=utf-8
# 字典排序 根据“键”或“键值”进行不同顺序的排序
"""
函数原型：sorted(iterable, cmp=None, key=None, reverse=False)
解释：iterable 可迭代类型
cmp为比较函数，
key为排序的对象（这里指键或键值），是迭代集合中的一项
reverse：注明升序还是降序，True--降序，False--升序（默认）
"""
dic = {'a': 31, 'bc': 5, 'c': 3, 'asd': 4, '33': 56, 'd': 0}

# dic.iteritems()，返回字典键值对的元组集合
print sorted(dic.iteritems(), key=lambda d: d[1], reverse=False)

# [('d', 0), ('c', 3), ('asd', 4), ('bc', 5), ('a', 31), ('33', 56)]
