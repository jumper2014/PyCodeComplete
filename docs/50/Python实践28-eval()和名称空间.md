### 介绍
- eval(expression, globals=None, locals=None) 可以对表达式求值，第一个参数可以为字符串，或者是内建函数compile()创建的预编译代码对象
- 第二，第三个参数可选，分别代表全局和局部名称空间的对象，如果给出这两个参数，globals必须是个字典，locals可以是任何映射对象

### 名称空间搜索顺序
当一行代码要使用变量 x 的值时，Python 会到所有可用的名字空间去查找变量，按照如下顺序:
1. 局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量 x, 或一个参数 x，Python 将使用它，然后停止搜索。
2. 全局名字空间 - 特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python 将使用它然后停止搜索。
3. 内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python 将假设 x 是内置函数或变量。

### 例子
```
# 全局名称空间
x = 5
y = 6
z = 7
res0 = eval('x+y')
# output: 11
print(res0)


def foo():
    x = 1
    y = 2

    # 局部名称空间
    res1 = eval('x+y')
    # output: 3
    print(res1)

    # 全局名称空间
    res2 = eval('x+y', globals())
    # output: 11
    print(res2)

    # 优先使用局部名称空间
    res3 = eval('x+y', globals(), locals())
    # output: 13
    print(res3)

    # 优先使用局部名称空间
    res3 = eval('x+y', globals(), locals())
    # output: 13
    print(res3)

    # 混杂使用名称空间
    res4 = eval('x+z', globals(), locals())
    # output: 8
    print(res4)


foo()
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/module/20180128)

如果觉得本文对您有帮助，敬请点赞。