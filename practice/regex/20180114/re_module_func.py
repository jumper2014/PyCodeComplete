#!/usr/bin/env python
# coding=utf-8
# 演示正则对象的用法
# 预编译正则表达式可以提升执行性能

import re


# match是从字符串开头开始匹配
m = re.match('.*com', 'www.baidu.com')
print(m)
result = m.group()
print(result)
# 输出www.baidu.com

# search是搜索第一次出现的位置
m = re.search('com', 'www.baidu.com')
print(m.group())
# 输出com


