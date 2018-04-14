#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


class User(object):
    def __init__(self, name):
        self.name = name
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 100 or value < 0:
            self._age = 0
        else:
            self._age = value


if __name__ == '__main__':
    user = User('Li')
    user.age = 101
    print(user.age)     # 0
