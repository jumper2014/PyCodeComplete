# coding=utf-8
__author__ = 'zengyuetian'

"""
将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
参数source：字符串或者AST（Abstract Syntax Trees）对象。
参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
参数flag和dont_inherit：这两个参数暂不介绍，可选参数。

版本：在python2.3、2.6、2.7、3.2中均有不同，使用时要引起注意，兼容python3
"""

code = "for i in range(0, 10):  print i"
cmpcode = compile(code, '', 'exec')
exec cmpcode


str = "3*4 + 5"
a = compile(str, '', 'eval')
print eval(a)
