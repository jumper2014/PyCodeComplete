### 背景
- 看《流畅的Python》第一章有个例子，里面用到了namedtuple，看了下和类很像，也有属性，区别就是不能直接改变属性值，但是不理解为什么要这样用。
- 网上也看了些中文资料，大多数都是讲如何用namedtuple，却没有找到它的适用场合，只好求助stackoverflow。

### 先看例子
- namedtuple是collections模块里面一个有名的数据容器类型
- namedtuple用来创建类似元组的数据类型，不仅可以用索引来访问数据，还能通过属性名来访问数据
- 如果要更新某个属性名的数据，需要使用特定的方法_replace()
- 下面请看例子：
```
from collections import namedtuple

if __name__ == '__main__':
    # 定义一个namedtuple类型User，并包含name，sex和age属性。
    User = namedtuple('User', ['name', 'sex', 'age'])

    # 创建一个User对象
    user = User(name='Li', sex='male', age=21)

    # 使用索引访问元素，output: Li
    print(user[0])

    # 使用属性访问元素，output: 21
    print(user.age)

    # 修改对象属性，注意要使用"_replace"方法
    user = user._replace(age=22)
    # output: 22
    print(user.age)
```

### 适用场合
- 当你觉得使用属性名代替索引更有意义更易读的时候，尤其是将他们传给其他函数的时候
- 可以用namedtuple代替那些不包含方法而且不可变的类对象


### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/collection/tuple/20180130)

如果觉得本文对您有帮助，敬请点赞。