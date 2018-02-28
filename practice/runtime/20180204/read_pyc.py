#!/usr/bin/env python
# coding=utf-8

import dis, marshal

if __name__ == '__main__':
    with open('hello.pyc', 'rb') as f:
        f.seek(8)
        dis.dis(marshal.load(f))