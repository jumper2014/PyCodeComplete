#!/usr/bin/env python
# coding=utf-8
# 在python2中，input()会把输入当做表达式进行运算，raw_input()把输入当做string返回
# 在python3中，raw_input()被删除，python3中的input()和python2中的raw_input()效果等同
# eval(input())和python2中的raw_input()效果等同

# 注，以下为方法示例，不能正常执行
# 必须有引号
name = input("what is your name")
print "hello ", name

# 不需要引号
name = raw_input("what is your name again")
print "hello ", name
