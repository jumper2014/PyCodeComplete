### 背景
- 内置函数repr是通过`__repr__`这个特殊方法来得到一个对象的字符串表示形式
- repr适用于交互式控制台和调试程序，用来获取字符串表示形式
- 类似的内置函数str使用的是`__str__`，它适用于print函数，它对终端用户更友好
- 如果想偷懒，可以只实现`__repr__`，因为如果一个对象没有`__str__`,而Python又需要调用它的时候，解释器会使用`__repr__`来代替

### 例子
```
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

    # 如果一个对象没有__str__,而Python又需要调用它的时候，解释器会使用__repr__来代替
    obj2 = YourClass()
    print(obj2)         # output: MyClassObj
```


### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/class/20180205)  
