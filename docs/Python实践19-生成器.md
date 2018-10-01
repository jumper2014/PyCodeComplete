### 生成器的出发点
- Python中迭代器可以用来遍历可迭代对象，但是需要通过实现一个迭代器类来完成
- Python可以通过调用函数达到类似迭代器的效果，这种函数就叫做生成器。

### 生成器语法
- Python中的生成器是一个带yield语句的函数
- 生成器运行到yield，会通过yield返回一个中间值给调用者，并且暂停执行。
- 当生成器的next()被调用的时候，它会从上次离开的地方继续执行。
- Python的for循环自带next()调用和对StopIteration的处理，常常用来迭代一个生成器

### 最佳用途
- 使用生成器最好的地方就是迭代一个巨大的数据集合时对每个元素进行及时的操作和处理

### 生成器实例
下面的例子，使用生成器来迭代素数
```
# 判断一个数字是否是素数
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(num)+1), 2):
            if num % current == 0:
                return False
        return True
    return False


# 生成器函数，start从什么位置开始向上查找素数
def get_primes(start):
    while True:
        if is_prime(start):
            yield start
        start += 1


if __name__ == "__main__":
    i = 0
    count = 10  # 一共查找多少个素数

    # 用for循环来迭代生成器
    for p in get_primes(2):
        print(p)
        i += 1
        if i >= count:
            break
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/generator/20180117)

