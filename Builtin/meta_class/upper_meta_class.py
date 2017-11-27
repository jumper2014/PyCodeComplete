# coding=utf-8
# 元类,是类的类
# 用来动态创建类
# 1)   拦截类的创建
# 2)   修改类
# 3)   返回修改之后的类


class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)


class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    __metaclass__ = UpperAttrMetaclass  # 这会作用到这个模块中的所有类
    bar = 'bip'

print hasattr(Foo, 'bar')
# 输出: False
print hasattr(Foo, 'BAR')
# 输出:True

f = Foo()
print f.BAR
# 输出:'bip'
