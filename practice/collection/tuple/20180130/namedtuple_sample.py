#!/usr/bin/env python
# coding=utf-8

from collections import namedtuple

if __name__ == '__main__':
    # 定义一个namedtuple类型User，并包含name，sex和age属性。
    User = namedtuple('User', ['name', 'sex', 'age'])

    # 创建一个User对象
    user = User(name='Li', sex='male', age=21)

    # 使用索引访问元素，output: Li
    print(user[0])

    # 使用属性访问元素，output: 21
    print(user.age)

    # 修改对象属性，注意要使用"_replace"方法
    user = user._replace(age=22)
    # output: 22
    print(user.age)
