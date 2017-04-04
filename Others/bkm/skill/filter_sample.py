# coding=utf-8
# filter的用法

lst = [1, 2, 3, 4, 5, 6]

# 所有奇数都会返回True, 偶数会返回False被过滤掉
print filter(lambda x: x % 2 != 0, lst)
# [1, 3, 5]


def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '   '])