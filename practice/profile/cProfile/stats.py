#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    import pstats

    # 创建Stats对象
    p = pstats.Stats("result.out")

    # strip_dirs(): 去掉无关的路径信息
    # sort_stats(): 排序，支持的方式和上述的一致
    # print_stats(): 打印分析结果，可以指定打印前几行

    # 按照函数名排序，只打印前3行函数的信息, 参数还可为小数,表示前百分之几的函数信息
    p.strip_dirs().sort_stats("name").print_stats(3)

    # 按照运行时间和函数名进行排序
    p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.8)

    # 如果想知道有哪些函数调用了bar
    p.print_callers("bar")

    # 查看test()函数中调用了哪些函数
    p.print_callees("foo")