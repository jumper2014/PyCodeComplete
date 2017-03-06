# coding=utf-8
# __eq__()用于判断对象内容是否相等

# is 当比较的是相同的对象实例时总是返回True
# == 取决于 __eq__()方法的实现


class A(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, obj):
        return self.name == obj.name


if __name__ == '__main__':
    a = A("Leon")
    b = A("Leon")
    print a == b  # True
    print a is b  # False


