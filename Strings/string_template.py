# coding=utf-8
# 格式化字符串

"""
Template无疑是一个好东西，可以将字符串的格式固定下来，重复利用。
同时Template也可以让开发人员可以分别考虑字符串的格式和其内容了，无形中减轻了开发人员的压力。
Template属于string中的一个类，所以要使用的话可以用以下方式调用
from string import Template
Template有个特殊标示符$,它具有以下的规则：
它的主要实现方式为$xxx,其中xxx是满足python命名规则的字符串，即不能以数字开头，不能为关键字等
如果$xxx需要和其他字符串接触时，可用{}将xxx包裹起来
"""

import string

values = {'name': 'jumper', 'age': 30}

t = string.Template("""
name    : $name
age     : ${age} years
Escape  : $$
""")

print 'TEMPLATE:', t.substitute(values)