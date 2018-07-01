### 装饰器的本质
Python里的装饰器是一个不太容易理解的东西，下面是一些关于Python装饰器的概念：
- 从形式上来说是在函数调用上的装饰
- 以@开头，接着是装饰器的名字和可选的参数
- 装饰器实质上是函数
- 装饰器的返回值是一个包装了的函数

### 装饰器的作用
装饰器用来装饰函数，可以在被装饰的函数调用前做些准备工作，在被装饰的函数调用后做些清理工作，这样的特征使它在AOP（Aspect Oriented Programming面向切面编程）方面被广泛利用。
一般装饰器可以用在下类场景中：
- 引入日志
- 计时，用于性能分析
- 给函数增加事务能力


### 举例
```
def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        ret = func(*args, **kwargs)
        print("delay 1 second to call %s" % func.__name__)
        return ret
    return wrapper


@delay
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, 2)
```
其中：
- add是被装饰的函数
- delay是装饰器
- wrapper调用被装饰的函数，并作为包装了的函数被返回，注意，Python里面函数就是对象，所以可以被直接返回。

凡是被delay装饰过的函数，都会自动被延迟一秒执行

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/decorator/20180114)