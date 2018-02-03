#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    # 将句子里面的单词抽取成元组
    txt = 'I like python and i use python'
    words = txt.split(' ')
    print(words)

    # 开始统计单词出现次数
    counts = dict()
    for word in words:
        counts[word] = counts.setdefault(word, 0) + 1
    print(counts)
