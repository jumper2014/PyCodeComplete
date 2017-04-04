# coding=utf-8

# 子类（派生类）并不会自动调用父类（基类）的init方法
# 需要子类主动调用父类的init

# 方法2


class Foo(object):
    def __init__(self):
        self.val = 1


class Foo2(Foo):
    def __init__(self):
        super(Foo2, self).__init__()
        print self.val


if __name__ == '__main__':
    foo2 = Foo2()