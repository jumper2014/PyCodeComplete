#!/usr/bin/env python
# coding=utf-8


class MyClass(object):
    def __repr__(self):
        return 'repr MyClassObj'

    def __str__(self):
        return 'MyClassObj'


class YourClass(object):
    def __repr__(self):
        return 'YourClassObj'

if __name__ == "__main__":
    obj = MyClass()
    print(repr(obj))    # output: repr MyClassObj
    print(str(obj))     # output: MyClassObj
    print(obj)          # output: MyClassObj

    # 如果一个对象没有`__str__`,而Python又需要调用它的时候，解释器会使用`__repr__`来代替
    obj2 = YourClass()
    print(obj2)         # output: MyClassObj
