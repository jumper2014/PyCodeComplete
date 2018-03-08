### 背景
- 我们常常会需要使用字典来统计序列里面各项出现的次数，key表示序列的项，value表示该项一共出现的次数
- 这种计数其实很简单，稍微麻烦一点的就是将出现的项初始化为0，以后每次出现都加1其实很简单
- 除了常规的每次判断该key有没有，然后根据情况初始为0然后加1，或者直接加1外，Python有两个很好用的方法可以解决这个问题。


### 使用dict自带的setdefault
- Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。如果键在字典中，返回这个键所对应的值。
- 原型 dict.setdefault(key, default=None)
- 一个例子如下
```
if __name__ == '__main__':
    # 将句子里面的单词抽取成元组
    txt = 'I like python and i use python'
    words = txt.split(' ')
    print(words)

    # 开始统计单词出现次数
    counts = dict()
    for word in words:
        counts[word] = counts.setdefault(word, 0) + 1
    print(counts)
```

### 使用collections的defaultdict模块
- defaultdict的定义如下class collections.defaultdict([default_factory[, ...]])
- default_factory 接收一个工厂函数作为参数, 例如int str list set等.该参数用于初始化该字典中不存在的key的value
- defaultdict在dict的基础上添加了一个missing(key)方法, 在调用一个不存的key的时候, defaultdict会调用__missing__, 返回一个根据default_factory参数的默认值, 所以不会返回Keyerror.
- 一个例子如下
```
# collections.defaultdict可以接受一个函数作为参数来初始化。
# 什么意思呢，我们想要frequencies[word]初始化为0，
# 这时就可以用一个int()函数作为参数出给defaultdict，我们不带参数调用int()，int()就会返回一个0值

from collections import defaultdict

if __name__ == "__main__":
    # 将句子里面的单词抽取成元组
    txt = 'I like python and i use python'
    words = txt.split(' ')
    print(words)

    # 开始统计单词出现次数
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    print(counts)
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得。  欢迎star该代码仓库
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/collection/dict/20180203)

如果觉得本文对您有帮助，敬请点赞。