#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import pstats

if __name__ == '__main__':
    # 创建Stats对象
    p = pstats.Stats("foo.out")

    # 这一行的效果和直接运行cProfile.run("foo()")的显示效果是一样的
    p.strip_dirs().sort_stats(-1).print_stats()