### 闭包定义
> In programming languages, closures (also lexical closures or function closures) are a technique for implementing lexically scoped name binding in languages with first-class functions.

解释：
> 在编程语言中，闭包（也词法闭包或函数闭包）是结合拥有 First-class function 的语言，实现词法作用域名的一种技术。

根据类型的值的可赋值状况，可以把类型分为三类
- 一级的（first-class）。该等级类型的值可以传给子程序作为参数，可以从子程序里返回，可以赋给变量。大多数程序设计语言里，整型、字符类型等简单类型都是一级的。 （Python中，函数就是一级的类型）
- 二级的（second-class）。该等级类型的值可以传给子程序作为参数，但是不能从子程序里返回，也不能赋给变量。
- 三级的（third-class）。该等级类型的值连作为参数传递也不行。

### Python中的闭包
- 定义：在一个内部函数里，对在外部作用域（但不是全局作用域）的变量进行引用，那么内部函数就被认为是闭包。
- 形式：内部函数引用外部函数的变量。外部函数返回内部函数。
- 作用：避免使用全局变量，隐藏内部数据；类的简单替代方式；


### 例子
下面我们举一个例子来展示如何使用闭包代替类。
```
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


class Multiplier(object):
    def __init__(self, faciend):
        self.faciend = faciend

    def product(self, multiplicator):
        return self.faciend * multiplicator

if __name__ == "__main__":
    # 使用闭包
    # Multiplier of 3
    times3 = make_multiplier_of(3)

    # Multiplier of 5
    times5 = make_multiplier_of(5)

    # Output: 27
    print(times3(9))

    # Output: 15
    print(times5(3))

    # 使用类
    # Output: 27s
    mul = Multiplier(3)
    print(mul.product(9))

    # Output: 15
    mul = Multiplier(5)
    print(mul.product(3))
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/closure/20180121)

如果觉得本文对您有帮助，敬请点赞。