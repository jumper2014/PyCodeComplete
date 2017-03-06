# coding=utf-8

"""
题意：给一个n*m的矩形，和a*a的正方形。要用a*a的正方形去覆盖n*m的矩形，
要求a*a的正方形不能切割开，但是两个a*a的正方形可以重叠，问最小需要几个这样的正方形
"""

my_list = raw_input().split()
n = int(my_list[0])
m = int(my_list[1])
a = int(my_list[2])

print (n / a + (n % a > 0)) * (m / a + (m % a > 0))
