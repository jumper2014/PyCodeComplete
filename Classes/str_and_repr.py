# coding=utf-8
# str()和repr()的区别

# str()面向用户， repr()面向程序员
# 一般类都应该定义__repr__(), __str__()可选
# 当没有__str__()的时候，默认用__repr__()来返回对象的字符串形式


class Class1(object):
    def __str__(self):
        return "str format"

    def __repr__(self):
        return "repr format"


class Class2(object):
    def __repr__(self):
        return "repr format"

if __name__ == "__main__":
    cl = Class1()
    print str(cl)
    print repr(cl)

    cl = Class2()
    print str(cl)
    print repr(cl)
