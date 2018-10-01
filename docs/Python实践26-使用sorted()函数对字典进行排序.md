### 背景
- 有的时候我们会将一些数据放在字典里，并且需要对这些键值对进行排序
- 例如某些项出现的次数或者频率，或者权重等等

### 解决方法
- 用字典存储这些数据
- 使用sorted()函数对字典中的键值对进行排序
- 由于sorted()函数需要接受一个可迭代对象，所以需要先将字典转换成可迭代的对象。使用字典的items()函数可以同时迭代key和value


### 代码实现
```
word_counts = {'love': 5, 'she': 9, 'he': 4}

# items()，返回字典键值对的list
sorted_count = sorted(word_counts.items(), key=lambda item: item[1], reverse=False)
print(sorted_count)
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/func/20180127)

如果觉得本文对您有帮助，敬请点赞。