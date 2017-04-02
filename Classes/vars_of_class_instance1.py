# coding=utf-8

# 类变量定义在类的定义之后，
# 实例变量则是以为self.开头


class Foo(object):
    val = 0

    def __init__(self):
        self.val = 1


if __name__ == '__main__':
    foo = Foo()
    print foo.val  # 1
    print Foo.val  # 0

