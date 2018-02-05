#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    # 没有遇到break, else就会被执行
    for i in range(2):
        print(i)
    else:
        print('loop done')

    # 遇到break， else不执行
    for i in range(2):
        if i == 1:
            break
        print(i)
    else:
        print('loop done')

    # 如果循环要迭代的序列是空的，else依然会被执行
    for i in []:
        print(i)
    else:
        print('loo done for empty list')