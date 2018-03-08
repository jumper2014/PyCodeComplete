### 无参数的装饰器
```
@delay
def add():
    pass
```
最后 add = delay(add)

### 带参数的装饰器
```
@delay(sec)
def add():
    pass
```
最后 add = delay(sec)(add)

例子如下：
```
def delay(sec):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            time.sleep(sec)
            ret = func(*args, **kwargs)
            print("delay %d seconds to call %s" % (sec, func.__name__))
            return ret
        return _wrapper
    return wrapper


@delay(2)
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, 2)
```
我们可以看到，让装饰器带参数，和不带参数的示例相比在外层多了一层包装。

### 多层装饰
Python里面，多个装饰器可以装饰在同一个函数上面。
```
@deco1(deco_arg)
@deco2
def func():
    pass
```
最后 func = deco1(deco_arg)(deco2(func))

```
@deco1
@deco2(deco_arg)
def func():
    pass
```
最后 func = deco1(deco2(deco_arg)(func))

下面是一个例子
```
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        cost = time.time() - start
        print("cost %f second " % cost)
        return ret
    return wrapper


def delay(sec):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            time.sleep(sec)
            ret = func(*args, **kwargs)
            print("delay %d seconds to call %s" % (sec, func.__name__))
            return ret
        return _wrapper
    return wrapper


@timeit
@delay(2)
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, 2)
```
结果如下：
> delay 2 seconds to call add  
> cost 2.000971 second 

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/decorator/20180114)