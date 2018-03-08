### 作用
- Python中map()函数能够通过函数处理序列
- 最终返回一个新的列表

### 形式
- map()函数接受两个参数，形如map(func, seq)
- 第一个参数func是一个函数
- 第二个参数seq是一个序列
- map()将函数func调用，一一映射到序列seq的每一个元素上
- 最终返回一个含有所有返回值的列表

### 例子
```
map(lambda x: x**2, range(10))
```

### 支持多序列参数
- map()能以多个序列作为其输入
- map()并行地迭代每个序列，将对应位置的元素绑定到一个元组
- 然后将函数func一一映射到这样的每一个元组上
- 最终返回一个含有所有返回值的列表

下面是一个例子：
```
map(lambda x, y: "{0} {1}".format(x, y), ["Zhang", "Li"], ["Yan", "Gang"])
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/func/20180118)

如果觉得本文对您有帮助，敬请点赞。