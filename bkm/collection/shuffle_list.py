# coding=utf-8
# 用随机顺序处理列表中的元素

import random

def process(elem):
    pass

def process_all_in_random_order(data, process):
    data = list(data)

    random.shuffle(data)
    for element in data:
        process(element)