# coding=utf-8
# 文本文件中替换字符串

import fileinput

# inplace=1：标准输出会被重定向到打开文件；backup='.bak'
# 替换文件内容之前备份后缀以_bak结尾；
for line in fileinput.input("infile_replace.txt", backup='.bak', inplace=1):
    print line.replace('abcd', 'OK')
fileinput.close()
