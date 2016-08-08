# coding=utf-8
"""
十进制数学计算
"""

from decimal import Decimal as D
from decimal import getcontext
print getcontext()

getcontext().prec = 20
print D(1)/D(3)
print 1.00/3.00

