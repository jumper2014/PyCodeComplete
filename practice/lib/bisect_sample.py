#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import bisect

if __name__ == '__main__':
    print(dir(bisect))
    data = [5, 7, 2, 9]
    data.sort()
    print(data) # [2, 5, 7, 9]

    # bisect函数不执行实际插入
    x = bisect.bisect(data, 3)
    print(x)    # 1
    print(data)     # [2, 5, 7, 9]

    # 执行实际插入
    bisect.insort(data, 3)
    print(data)     # [2, 3, 5, 7, 9]

    # 靠左
    x = bisect.bisect_left(data, 5)
    print(x)  # 2
    # 靠右
    x = bisect.bisect_right(data, 5)
    print(x)   # 3

    # 实际插入
    bisect.insort_left(data, 5)
    bisect.insort_right(data, 5)
    print(data)  # [2, 3, 5, 5, 5, 7, 9]