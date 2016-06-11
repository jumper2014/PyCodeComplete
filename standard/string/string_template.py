# coding=utf-8
# 格式化字符串

import string

values = {'name': 'jumper', 'age': 30}

t = string.Template("""
Name    : $name
Age     : ${age} years
Escape  : $$
""")

print 'TEMPLATE:', t.substitute(values)