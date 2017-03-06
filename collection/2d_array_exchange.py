# coding=utf-8
# 二维阵列变换

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print map(list, zip(*arr))