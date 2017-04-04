# coding=utf-8
from __future__ import division

# 是否是小数部分
isDecimal = False
# 第几位小数位
decimalBit = 0


# reduce函数
def fn(x, y):
    global isDecimal
    global decimalBit
    if y == '.':  # 小数部分开始
        isDecimal = True
        return x

    if not isDecimal:  # 整数部分
        return x * 10 + y
    else:  # 小数部分
        decimalBit += 1
        return x + y / (10 ** decimalBit)


# 字符转数字
def char2num(s):
    dictionary = {'0': 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ".": "."}
    return dictionary[s]


# 计算结果
print reduce(fn, map(char2num, "0123.04567890"))
