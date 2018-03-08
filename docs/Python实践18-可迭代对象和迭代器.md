### 可迭代对象和迭代器
- 可以用for循环遍历的对象统称为可迭代对象(Iterable)
- 可以被next()函数调用，不断返回下一个值的对象被成为迭代器(Iterator)
- 可迭代对象的for循环的实际是靠不断将可迭代对象的迭代器传给next()调用实现的。

### 生成迭代器
在可迭代对象上调用iter()，就会生成一个迭代器。即 迭代器 = iter(可迭代对象)  
所以，可迭代对象必须内部实现__iter__()函数，返回一个迭代器。

但是迭代器也不是任何对象都可以充当的，必须要满足迭代器协议：
- 内部实现__iter__()函数，返回迭代器对象本身
- 内部实现next()函数(Python3是__next__()函数)，返回下一个元素，遍历完成时需要抛出StopIteration异常。


### 示例
假设我们要遍历一个可迭代对象，该对象里面存储了不同年龄的用户信息，我们希望能用for循环遍历那些年龄超过18岁的成年用户。
所以，我们需要自定义两个类：
- 可迭代对象AdultIterable(实现__iter__()函数)
- 迭代器AdultIterator(实现__iter__()和next()函数)
 
```
class AdultIterable(object):
    def __init__(self, ages):
        self.__ages = ages

    def __iter__(self):
        print("call iterable __iter__()")
        return AdultIterator([x for x in self.__ages if x >= 18])


class AdultIterator(object):
    def __init__(self, data):
        self.__data = data
        self.__index = 0

    def __iter__(self):
        return self

    def next(self):
        print("call iterator next()")
        if self.__index < len(self.__data):
            val = self.__data[self.__index]
            self.__index += 1
            return val
        else:
            raise StopIteration


if __name__ == "__main__":
    user_ages = list(range(12, 60))
    ages = AdultIterable(user_ages)  # 生成一个可迭代对象

    age = iter(ages)    # 生成一个迭代器
    print(next(age))   # 用迭代器来遍历可迭代对象
    print(next(age))   # 用迭代器来遍历可迭代对象

    for age in ages:    # 用for来遍历
        print age
```


### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/blob/master/practice/iterator/20180115/adult_iterator.py)
 




