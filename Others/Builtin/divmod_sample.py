# coding=utf-8
__author__ = 'zengyuetian'

"""
divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数
返回结果类型为tuple
参数：
a,b可以为数字（包括复数）
版本：
在python2.3版本之前不允许处理复数，这个大家要注意一下
"""

print divmod(9, 2)
print divmod(11, 3)
print divmod(1+2j, 1+0.5j)

