# coding=utf-8
# 计算文件行数

thefilepath = "file.txt"
count = len(open(thefilepath, 'rU').readlines())
print count
