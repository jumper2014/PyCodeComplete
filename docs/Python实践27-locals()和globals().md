### 简介
- locals()和globals()分别用来返回调用者的局部和全局名称空间的字典。
- 在全局名称空间下，globals()和locals()返回相同的字典。
- 通过这两个函数，可以在局部名称空间中访问全局名称空间的变量

### 例子
下面展示了如何在局部名称空间中访问全局名称空间的变量
```
def foo():
    num = 10
    # 在局部名称空间中访问全局名称空间的变量
    # output: ('foo globals-num', 5)
    print("foo globals-num", globals()['num'])

    # output: ('foo locals-num', 10)
    print("foo locals-num", locals()['num'])


num = 5
foo()

# 在全局名称空间下，globals()和locals()返回相同的字典。
print("globals", globals())
print("locals", globals())
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/module/20180127)

如果觉得本文对您有帮助，敬请点赞。