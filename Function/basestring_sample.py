# coding=utf-8
"""
basestring是str和unicode的超类（父类），也是抽象类，因此不能被调用和实例化，
但可以被用来判断一个对象是否为str或者unicode的实例，isinstance(obj, basestring)等价于isinstance(obj, (str, unicode))；
版本：python2.3版本以后引入该函数，兼容python2.3以后python2各版本。注意：python3中舍弃了该函数，所以该函数不能在python3中使用。
"""

print isinstance("Hello world", str)
# True

print isinstance("Hello world", basestring)
# True

print isinstance(u"你好", unicode)
# True

print isinstance(u"你好", basestring)
# True
