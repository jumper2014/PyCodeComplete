#!/usr/bin/env python
# coding=utf-8

# collections.defaultdict可以接受一个函数作为参数来初始化。
# 什么意思呢，我们想要frequencies[word]初始化为0，
# 这时就可以用一个int()函数作为参数出给defaultdict，我们不带参数调用int()，int()就会返回一个0值

from collections import defaultdict

if __name__ == "__main__":
    # 将句子里面的单词抽取成元组
    txt = 'I like python and i use python'
    words = txt.split(' ')
    print(words)

    # 开始统计单词出现次数
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    print(counts)

