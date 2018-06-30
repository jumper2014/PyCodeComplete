#!/usr/bin/env python
# coding=utf-8
# partial()函数的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


from functools import partial

if __name__ == "__main__":
    standard = "User N"

    # 用偏函数构造一个新的函数
    usern = partial(standard.replace, "N")

    # output: User 1
    print(usern("1"))

    # output: User 9527
    print(usern("9527"))
