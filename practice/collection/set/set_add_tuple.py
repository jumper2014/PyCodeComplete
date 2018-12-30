#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    myset = set()
    myset.add(("1", "2", "3"))
    myset.add(("1", "2", "1"))
    myset.add(("1", "2", "3"))

    print(myset)