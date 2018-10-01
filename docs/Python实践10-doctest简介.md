### doctest的作用
- 在python代码中寻找类似交互解释器里执行的命令，执行它们并且和这些命令的期望值进行比较。
- 用来验证docstring中的注释和代码实际的作用是一致的
- 可以作为回归测试来验证代码能够正确执行
- 可以用来编写模块的文档演示这些模块是如何处理输入得到输出的。

### doctest的要点
- 一般写在函数的docstring里面
- 用>>>表示一个用例的开始，直到遇到空行或者下一个>>>
- 使用#doctest: +ELLIPSIS（中文含义省略）来表示下面的省略号匹配任意内容
- 执行时默认只打印出错的用例结果，如果使用类似python sample.py -v的命令行 将会打印所有测试用例的结果。


### 一个例子
```
def add(x, y):
    """ add two number or string
    >>> add(1, 2)
    3

    >>> add("hello", " world")
    'hello world'

    >>> add(1, 2.0)
    3

    >>> add("hello", " python")  # doctest: +ELLIPSIS
    'hello ...'

    """
    return x+y


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

执行它python doctest_sample.py -v得到结果如下(3个用例pass，1个用例fail)：
```
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add("hello", " world")
Expecting:
    'hello world'
ok
Trying:
    add(1, 2.0)
Expecting:
    3
**********************************************************************
File "doctest_sample.py", line 13, in __main__.add
Failed example:
    add(1, 2.0)
Expected:
    3
Got:
    3.0
Trying:
    add("hello", " python")  # doctest: +ELLIPSIS
Expecting:
    'hello ...'
ok
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
   1 of   4 in __main__.add
4 tests in 2 items.
3 passed and 1 failed.
***Test Failed*** 1 failures.
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/lib/test/20180223)