#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import math


def cal_entropy(text):
    h = 0.0
    sum = 0
    letter = [0] * 26
    text = text.lower()
    for i in range(len(text)):
        if text[i].isalpha():
            letter[ord(text[i]) - ord('a')] += 1
            sum += 1
    print('\n', letter)
    for i in range(26):
        p = 1.0 * letter[i] / sum
        if p > 0:
            h += -(p * math.log(p, 2))
    return h


if __name__ == '__main__':
    sentence = "This is a sample for python language"
    print("entropy is: {0}".format(cal_entropy(sentence)))
