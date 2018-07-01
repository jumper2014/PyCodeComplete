### 特殊语法
- 本文内容来自《effective python》
- Python中有种特殊语法，可在for及while循环的内部语句块之后紧跟一个else块
- 只有当整个循环主题都没有遇到break语句时，循环后面的else块才会执行
- 不要在循环后面使用else块的写法。因为这种写法既不直观，又容易引起误解
- 为了看懂别人的代码，所以本文还是演示一下这两种用法。

### for循环和else
```
if __name__ == '__main__':
    # 没有遇到break, else就会被执行
    for i in range(2):
        print(i)
    else:
        print('loop done')

    # 遇到break， else不执行
    for i in range(2):
        if i == 1:
            break
        print(i)
    else:
        print('loop done')

    # 如果循环要迭代的序列是空的，else依然会被执行
    for i in []:
        print(i)
    else:
        print('loo done for empty list')
```


### while循环和else
```
if __name__ == '__main__':
    # 没有遇到break, else就会被执行
    i = 0
    while i < 2:
        print(i)
        i += 1
    else:
        print('loop done')

    # 遇到break， else不执行
    i = 0
    while i < 2:
        if i == 1:
            break
        print(i)
        i += 1
    else:
        print('loop done')
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/syntax/loop/20180205)  
