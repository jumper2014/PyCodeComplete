#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    # 没有遇到break, else就会被执行
    i = 0
    while i < 2:
        print(i)
        i += 1
    else:
        print('loop done')

    # 遇到break， else不执行
    i = 0
    while i < 2:
        if i == 1:
            break
        print(i)
        i += 1
    else:
        print('loop done')
