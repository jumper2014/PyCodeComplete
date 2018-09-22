#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def add(a, b):
    return a + b


c = add.__code__
print('函数名称:', c.co_name)
print('位置参数的个数:', c.co_argcount)
print('函数使用的局部变量个数:', c.co_nlocals)
print('包含局部变量名的元组:', c.co_varnames)
print('原始字节码的字符串:', c.co_code)
print('字节码所用字面量的元组:', c.co_consts)
print('字节码所用名称的元组:', c.co_names)
print('被编译代码所在文件的名称:', c.co_filename)
print('函数的首行行号:', c.co_firstlineno)
print('所需栈的大小:', c.co_stacksize)
print('包含解释器标志的整数:', c.co_flags)

"""
函数名称: add
位置参数的个数: 2
函数使用的局部变量个数: 2
包含局部变量名的元组: ('a', 'b')
原始字节码的字符串: b'|\x00|\x01\x17\x00S\x00'
字节码所用字面量的元组: (None,)
字节码所用名称的元组: ()
被编译代码所在文件的名称: /Users/zyt/git/github/PyCodeComplete/practice/runtime/code_block.py
函数的首行行号: 6
所需栈的大小: 2
包含解释器标志的整数: 67
"""

