# coding=utf-8
# 类的静态变量

# Variables declared inside the class definition, but not inside a method are class or static variables

class MyClass:
     i = 3

# this creates a class-level "i" variable, but this is distinct from any instance-level "i" variable, so you could have

cl = MyClass()

cl.i = 4
print cl.i
print MyClass.i