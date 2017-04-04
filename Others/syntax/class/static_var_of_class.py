# coding=utf-8
# 类的静态变量


class MyClass(object):
    i = 3


m = MyClass()
m.i = 4

print(MyClass.i)     # 3
print(m.i)           # 4

# 上面的i变量是类级别的,它和所有的实体对象的i不一样
