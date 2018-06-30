#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    # 把平方计算结果打印在同一行
    for i in range(10):
        print("{0}*{0}".format(i), i*i, sep="=", end="\t")