#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


class Student(object):
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = 0


if __name__ == '__main__':
    try:
        s = Student('Li', 20)
    except Exception as e:
        print(e)
        # 'Student' object has no attribute 'grade'
