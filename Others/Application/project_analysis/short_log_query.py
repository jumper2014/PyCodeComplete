#!/usr/bin/python
# -*- coding:utf-8 -*-

# 将日志中行超过特定长度的行去除，用剩下的行生成一个新文件

length = 500

if __name__ == "__main__":
    i = 0

    new_file = open("query.log.new", "w+")

    for line in open("/query.shop.log"):
        if len(line) > length:
            i += 1
            if i % 100 == 0:
                print 'line goes ', i
        else:
            new_file.writelines(line)
            pass
    print 'total lines ', i
