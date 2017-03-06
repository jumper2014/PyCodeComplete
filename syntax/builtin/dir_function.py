# coding=utf-8
# dir()和__dir__()函数
# 当你为dir提供一个模块名的时候，它返回模块定义的名称列表。
# 如果不提供参数，它返回当前模块中定义的名称列表


class NotDefine(object):
    pass


class Shape(object):
    def __dir__(self):
        return ['area', 'perimeter', 'location']

# ['NotDefine', 'Shape', '__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'struct']
print dir()

# ['Struct', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_clearcache', 'calcsize', 'error', 'pack', 'pack_into', 'unpack', 'unpack_from']
import struct
print dir(struct)

# ['area', 'location', 'perimeter']
s = Shape()
print dir(s)

# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
n = NotDefine()
print dir(n)