### 偏函数简介
- 偏函数是从Python2.5引入的一个概念，通过functools模块被用户调用
- 偏函数是将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数依次作为partial()函数后续的参数，除非使用关键字参数
- partial()函数的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


### 例子
下面的例子展示了如何使用偏函数生成一个新的函数
```
from functools import partial

if __name__ == "__main__":
    standard = "User N"

    # 用偏函数构造一个新的函数
    usern = partial(standard.replace, "N")

    # output: User 1
    print(usern("1"))

    # output: User 9527
    print(usern("9527"))
```


### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/func/20180123)

如果觉得本文对您有帮助，敬请点赞。