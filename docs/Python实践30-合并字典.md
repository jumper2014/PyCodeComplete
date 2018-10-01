### 合并字典的几种方法
- 获取字典的键值对的列表,拼成一个新的列表,将合并成的列表转变成新的字典
- 使用dict()初始化函数
- 使用字典的update()函数
- 循环字典键值对，然后放入同一个字典（最笨重，不使用）

### 处理冲突
- 待合并的几个字典中可能有重复的key
- 对待冲突，后面调用的字典的内容会覆盖前面的

### 例子
下面的例子演示了如何合并字典，推荐使用方法3，也就是使用update()函数
```
    # 定义两个有重复key的字典
    dict1 = {'usr': 'root', 'pwd': '123'}
    dict2 = {'ip': '192.168.1.1', 'usr': 'admin'}

    # 方法1
    # 获取字典的键值对的列表
    # 拼成一个新的列表
    # 将合并成的列表转变成新的字典
    # print(dict1.items())
    # print(dict2.items())
    # print(dict1.items() + dict2.items())
    dict3 = dict(dict1.items() + dict2.items())
    # output: {'ip': '192.168.1.1', 'pwd': '123', 'usr': 'admin'}
    print(dict3)

    # 方法2
    # 使用初始化函数
    dict4 = dict(dict1, **dict2)
    # output: {'ip': '192.168.1.1', 'pwd': '123', 'usr': 'admin'}
    print(dict4)

    # 方法3
    # 相同的key，后面的dict覆盖前面的dict
    dict2.update(dict1)
    # output: {'ip': '192.168.1.1', 'pwd': '123', 'usr': 'root'}
    print(dict2)
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/collection/dict/20180129)

如果觉得本文对您有帮助，敬请点赞。