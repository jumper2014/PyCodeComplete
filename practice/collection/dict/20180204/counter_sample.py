#!/usr/bin/env python
# coding=utf-8


from collections import Counter

if __name__ == "__main__":
    # 将句子里面的单词抽取成元组
    txt = 'I like python and i use python'
    words = txt.split(' ')
    print(words)

    # 一行代码搞定
    counter = Counter(words)
    print(dict(counter))