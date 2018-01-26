#!/usr/bin/env python
# coding=utf-8
# 演示正则对象的用法
# 预编译正则表达式可以提升执行性能

import re

p = re.compile('.*com')
print(p)
# match是从字符串开头开始匹配
m = p.match('www.baidu.com')
result = m.group()
print(m)
print(result)
# 输出www.baidu.com

# search是搜索第一次出现的位置
p = re.compile('com')
m = p.search('www.baidu.com')
print(m.group())
# 输出com