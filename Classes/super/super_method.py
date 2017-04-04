# coding=utf-8
# super用来执行父类中的函数


class Foo(object):
    def hi(self):
        print 'hi,Foo'


class Foo2(Foo):
    def hi(self):
        super(Foo2, self).hi()


if __name__ == '__main__':
    foo2 = Foo2()
    foo2.hi()
