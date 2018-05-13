#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import dis


def foo():
    pass


if __name__ == '__main__':
    print(dis.dis(foo))