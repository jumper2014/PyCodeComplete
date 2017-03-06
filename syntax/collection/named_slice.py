# coding=utf-8
# 命名切片

a = [0, 1, 2, 3, 4, 5]

# slice(start, end, step)
LASTTHREE = slice(-3, None)
print LASTTHREE
print a[LASTTHREE]