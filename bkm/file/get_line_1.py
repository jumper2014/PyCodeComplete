# coding=utf-8
# 根据指定的行号,从文本文件中读取一行数据

# linecache读取并缓存你指定名字的文件中的所有文本
# 所以对于大文件慎重使用

import linecache
thefilepath = "file.txt"
desired_line_number = 5
theline = linecache.getline(thefilepath, desired_line_number)
print theline
