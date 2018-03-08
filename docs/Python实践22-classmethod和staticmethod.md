### 介绍
> @classmethod means: when this method is called, we pass the class as the first argument instead of the instance of that class (as we normally do with methods). This means you can use the class and its properties inside that method rather than a particular instance.
> @staticmethod means: when this method is called, we don't pass an instance of the class to it (as we normally do with methods). This means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not use the instance).

- classmethod()和staticmethod()可以将类里面的函数转换成类方法和静态方法。在Python2.4以后可以用装饰器@classmethod和@staticmethod来代替他们。
- 类方法被调用的时候，将会把类作为第一个参数传给方法，这意味着你可以在该方法里面使用类的相关属性，而不是某个实例的属性。
- 静态方法被调用的时候，不会传递类的实例给该方法，这意味着你仅仅将该方法放在类里，而无法在该方法里访问该类的实例。

### 作用
- @classmethod主要用在那些需要访问类属性的方法上，常常用来作为构造函数的补充。
- @staticmethod主要用途是限定namespace，避免方法扩散，将与类相关的方法整合到类里面。

### 调用限制
- 类可以调用类方法和静态方法
- 类的实例也可以调用类方法和静态方法，但是从语义上来说，我强烈反对这样做。

### 实例
下面是一个来自于stackoverflow的例子，其中的@classmethod作为另类的构造函数，而@staticmethod用作类相关的辅助方法。
```
class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


if __name__ == "__main__":
    date2 = Date.from_string('11-09-2012')
    is_date = Date.is_date_valid('11-09-2012')
    print(is_date)
```


### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/class/20180122)

如果觉得本文对您有帮助，敬请点赞。