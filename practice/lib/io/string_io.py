#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import io

if __name__ == '__main__':

    output = io.StringIO()
    output.write('First line.\n')
    print('Second line.', file=output)

    # 获得对象内容
    contents = output.getvalue()
    print(contents)
    """
    First line.
    Second line.
    """

    # 关闭对象，并且丢弃内存缓存
    # 如果此后再调用getvalue()将会抛出异常
    output.close()

    # 通过初始化函数创建对象
    f = io.StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':     # 如果到达结尾
            break
        print(s.strip())
    f.close()
    """
    Hello!
    Hi!
    Goodbye!
    """
