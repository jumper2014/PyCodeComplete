### 多重继承和MRO
- Python支持多重继承
- MRO指的是Method Resolution Order，是用来在多重继承中搜索当前子类未定义属性的算法
- Python先后有三种不同的MRO：经典方式、Python2.2 新式算法、Python2.3 新式算法(C3)。Python 3中只保留了最后一种，即C3算法。
- C3算法解决了前两种算法遇到菱形继承结构时的不足
- Python2使用inspect.getmro(D)来查看MRO顺序
- Python3使用`D.__mro__`来查看MRO顺序

### 一个菱形结构继承的例子
```
class A():
    def who_am_i(self):
        print("I am A")


class B(A):
    pass


class C(A):
    def who_am_i(self):
        print("I am C")


class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
    d.who_am_i()    # I am C
    
    print(D.__mro__)
    # (<class '__main__.D'>, < class '__main__.B' >, < class '__main__.C' >, < class '__main__.A' >, < class 'object' > )

```