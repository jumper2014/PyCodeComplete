# coding=utf-8

age = 35
print age.__class__

name = 'bob'
print name.__class__


def foo():
    pass
print foo.__class__


class Bar(object):
    pass

b = Bar()
print b.__class__

print age.__class__.__class__
print name.__class__.__class__
print foo.__class__.__class__
print b.__class__.__class__

# type就是python的内建元类

# <type 'int'>
# <type 'str'>
# <type 'function'>
# <class '__main__.Bar'>
# <type 'type'>
# <type 'type'>
# <type 'type'>
# <type 'type'>