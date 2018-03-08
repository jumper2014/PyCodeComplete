### 布尔值
- 所有标准对象均可用于布尔测试，每个对象天生具有布尔True或False
- 空对象, 值为零的任何数字或者None的布尔值都是False
- 用户创建的类实例如果定义了nonzero(`__nonzero__`())或length(`__len__`())且值为0，那么他们的布尔值就是False。如果nonzero和length同时存在，以nonzero的结果为准。

### 标准对象里的False
```
def print_boolean_value(value):
    if value:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    # 下面所有的结果都是False
    print_boolean_value(None)
    print_boolean_value(False)
    # 所有值为0的数
    print_boolean_value(0)
    print_boolean_value(0.0)
    print_boolean_value(0L)
    print_boolean_value(0.0 + 0.0j)
    print_boolean_value("")
    print_boolean_value([])
    print_boolean_value(())
    print_boolean_value({})
```


### 自定义类实例的False
```
class A(object):
    def __nonzero__(self):
        return False


class B(object):
    def __len__(self):
        return 0


class C(object):
    def __nonzero__(self):
        return False

    def __len__(self):
        return 1


class D(object):
    pass


if __name__ == '__main__':
    # 下面的结果是False
    print_boolean_value(A())
    print_boolean_value(B())
    print_boolean_value(C())
    # 下面的结果是True
    print_boolean_value(D())
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得。  欢迎star该代码仓库
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/type/20180204)

如果觉得本文对您有帮助，敬请点赞。