#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import dis


def foo():
    print('foo')


if __name__ == '__main__':
    print(dis.dis(foo))
