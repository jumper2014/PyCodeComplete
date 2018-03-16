# coding=utf-8
# Python base64模块是用来作base64编码解码的。

"""
Python base64模块真正用的上的方法只有8个，
分别是encode, decode, encodestring, decodestring, b64encode,b64decode, urlsafe_b64decode,urlsafe_b64encode。
他们8个可以两两分为4组，encode,decode一组，专门用来编码和解码文件的,也可以对StringIO里的数据做编解码；
encodestring,decodestring一组，专门用来编码和解码字符串；
b64encode和b64decode一组，用来编码和解码字符串，并且有一个替换符号字符的功能。
这个功能是这样的：因为base64编码后的字符除了英文字母和数字外还有三个字符 + / =, 其中=只是为了补全编码后的字符数为4的整数，
而+和/在一些情况下需要被替换的，b64encode和b64decode正是提供了这样的功能。
至于什么情况下+和/需要被替换，最常见的就是对url进行base64编码的时候。
urlsafe_b64encode和urlsafe_b64decode 一组，这个就是用来专门对url进行base64编解码的，实际上也是调用的前一组函数。
"""

import base64

a = base64.b64encode('binary\x00string')
print a

b = base64.b64decode(a)
print b

print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')

print base64.urlsafe_b64decode('abcd--__')

# encode函数和decode函数的参数也可以是文件对象
# f1 = open('aaa.txt', 'r')
# f2 = open('bbb.txt', 'w')
# base64.encode(f1, f2)
# f1.close()
# f2.close()

