#!/usr/bin/python
# -*- coding:utf-8 -*-

# 获得log文件行数, 以及最长的行的长度

# http://stackoverflow.com/questions/2659952/maximum-length-of-http-get-request
# Most web servers have a limit of 8192 bytes (8KB)

if __name__ == "__main__":
    i = 0
    length = 0

    for line in open("query.shop.log"):
        i += 1
        if len(line) > length:
            length = len(line)

    print 'total lines ', i
    print 'max len is : ', length
