#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import psutil
import os


class Student1(object):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


if __name__ == '__main__':
    process = psutil.Process(os.getpid())
    mem_1 = process.memory_info().rss
    print('mem1:', mem_1)
    s = [Student1('python', 20, x) for x in range(1000 * 1000)]
    mem_2 = process.memory_info().rss
    print('mem2:', mem_2)
    print('noslot_mem:', mem_2 - mem_1)


