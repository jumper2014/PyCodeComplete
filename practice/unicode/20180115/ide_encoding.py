#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import codecs
print sys.getdefaultencoding()
# output: ascii
s = '你好'
print(s)
print(isinstance(s, unicode))
# output: False

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
# output: utf-8

s = '你好'
print(s)
print(isinstance(s, unicode))
# output: False
print(s.__class__)
# output: <type 'str'>
print(unicode(s).encode("utf-8"))
# print(unicode(s).encode("gbk"))   # for windows cmd

s = u'你好'
print(s)
print(isinstance(s, unicode))
# output: True
print(s.__class__)
# output: <type 'unicode'>

f = open('text.txt')
s = f.read()
f.close()
print type(s)  # <type 'str'>
# 已知是utf-8编码，解码成unicode，然后再编码成为gbk
u = s.decode('utf-8').encode('gbk')
print(u)

f = open('text1.txt', 'w')
# 编码成UTF-8编码的str
# s = u.decode('gbk').encode('UTF-8')
f.write(u)
f.close()


f = codecs.open('text.txt', encoding='UTF-8')
u = f.read()
f.close()
print(type(u))  # <type 'unicode'>
print(u)
print(u.encode("gbk"))