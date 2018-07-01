### 背景
- 默认情况下，自定义的类实例总被认为是真的，除非该类定义了`__bool__`或者`__len__`方法。
- 当使用bool(obj)来获得对象的布尔值的时候，优先使用`__bool__`方法的结果。
- 上面的规则针对Python3有效，因为`__bool__`不是Python2的内置方法。
- 在PyCharm等编辑器里面使用Python2的环境时，可以看出类的`__bool__`方法与其他魔法方法颜色不同

### 例子
```
class MyClass(object):
    def __init__(self):
        pass

    def __bool__(self):
        return False

    def __len__(self):
        return 1


def print_boolean_value(value):
    if value:
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    obj = MyClass()
    # output: False
    print_boolean_value(obj)
```


### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/class/20180205)  
