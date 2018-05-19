### 匿名函数和lambda表达式
- 匿名函数是指不用def形式声明的函数
- Python允许用lambda关键字创建匿名函数
- lambda表达式的返回是一个可调用的函数对象
- lambda表达式的形式为：lambda [arg1 [, arg2, ...]]: expression

### lambda表达式的特点
- 只能由一条表达式组成
- 一般在高阶函数中使用lambda表达式作为参数
- 精简的函数定义方式可以减少代码行数
- 调用处即定义有时可以提高代码可读性
- 可以用来实现闭包

### 简单例子
```
squares = map(lambda x: x**2, range(10))
print(squares)
```