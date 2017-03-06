# coding=utf-8
# 用reduce求和

def add(x, y):
    return x + y


sum = reduce(add, range(101))
print sum


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[s]


print reduce(fn, map(char2num, "123456"))
