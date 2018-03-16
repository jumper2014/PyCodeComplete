# coding=utf-8

# 实例也能够访问类变量，如下：
# 复制代码


class Foo(object):

    val = 0

    def __init__(self):
        pass

if __name__ == '__main__':
    foo = Foo()
    print foo.val  # 0
    print Foo.val  # 0
