# coding=utf-8

import copy

print [n for n in dir(copy) if not n.startswith('_')]

# __all__表示 从模块导入所有名字代表什么含义 from copy import *
# __all__会将没有指定的变量，类和函数过滤出去
# 如果没有定义__all__, import *会默认导入所有不以下划线开头的全局名称
print copy.__all__