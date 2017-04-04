# coding=utf-8
# 使用下划线忽略不关心的变量

data = ['ACME', 50, 91.1, (2012, 12,21)]
_, shares, price, _ = data
print shares
