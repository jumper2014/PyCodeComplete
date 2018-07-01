### 两种对象和三种角色
Python里面的正则表达式模块是re，大家常常看到两种语法形式，一种是类似re.match(), 另一种是p.match(),要想弄清楚他们的区别，就要从re的两种对象和正则表达式的三种角色说开去。

re模块里有两种对象
- 正则表达式对象(regex object)。
- 匹配对象(match object)。

正则表达式运算里面有三种角色
- 待匹配字符串
- 正则表达式
- 匹配结果

我们可以很容易发现，正则表达式对象和正则表达式对应，匹配结果和匹配对象对应。待匹配字符串就是正则表达式方法的输入。

所以一个基本的正则表达式计算有如下两步：
1. 根据正则表达式对象和待匹配字符串获得匹配对象
2. 根据匹配对象获得匹配结果

### 基本例子
```
import re
m = re.match('.*com', 'www.baidu.com')  # 对应步骤1,参数1是正则表达式，参数2是待匹配字符串，结果是匹配对象
result = m.group()  # 对应步骤2
print(result)
```

### 编译正则表达式对象
预编译正则表达式能够提升执行性能，使用的方法是re.compile()
```
import re
p = re.compile('.*com')  # 预编译步骤，生成正则表达式对象
m = p.match('www.baidu.com') # 对应步骤1
result = m.group()  # 对应步骤2
print(result)
```

### match()和search()
match()的search()是re模块里最常用的两个方法，下面是他们的区别。
- match(): 从待匹配串开头尝试对模式进行匹配
- search(): 待匹配串任意位置是否能满足模式匹配

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/regex/20180114)