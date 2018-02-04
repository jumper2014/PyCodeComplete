#!/usr/bin/env python
# coding=utf-8

if __name__ == "__main__":
    # 将句子里面的单词抽取成元组
    txt = 'I like python and i use python'
    words = txt.split(' ')
    print(words)

    words_set = set(words)
    counts = dict()
    for word in words_set:
        counts[word] = words.count(word)
    print(counts)