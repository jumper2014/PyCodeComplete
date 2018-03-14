### getattr()函数
- getattr()函数是普通函数，它和特殊函数__getattr__()不是一回事
- getattr()函数会在你试图读取一个不存在的属性时，引发AttributeError异常。


### `__getattr__()`函数
- `__getattr__()`函数是特殊函数
- 它仅当属性不能在实例的__dict__或它的类，或者祖先类中找到时，才被调用。
- 程序员主要用__getattr__()来实现类的灵活性，或者用它来做一些兜底的操作。
- 绝大多数情况下，你需要的是__getattr__()


### `__getattribute__()`函数
- `__getattribute__()` 在查找真正要访问的属性之前就被调用了，无论该属性是否存在。
- 使用`__getattribute__()`要特别注意，因为如果你在它里面不知何故再次调用了`__getattribute__()`，你就会进入无穷递归。为了避免这种情况，如果你想要访问任何它需要的属性，应该总是调用祖先类的同名方法：比如super(obj, self).`__getattribute__(attr)`
- 程序员主要使用__getattribute__()来实现某些拦截功能，特别是数据访问保护。例如下面这个例子将不允许访问对象的current元素：
```
class Count(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current = None

    def __getattribute__(self, item):
        print(type(item), item)
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self, item)
        # or you can use ---return super().__getattribute__(item)


obj1 = Count(1, 10)
print(obj1.min)
print(obj1.max)
print(obj1.current)
```

### 调用顺序
- 如果你的类同时存在__getattr__()和__getattribute__()，并且如果__getattribute__()抛出了AttributeError异常，那么该异常将会被忽略，__getattr__()依然会被调用。下面是一个例子：
```
class Count(object):
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax
        self.current = None

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self, item)
        # or you can use ---return super().__getattribute__(item)
        # note this class subclass object


obj1 = Count(1, 10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.current)

# 1
# 10
# 0
```

### 代码下载
本文内容和代码已经归档到https://github.com/jumper2014/PyCodeComplete，欢迎star

