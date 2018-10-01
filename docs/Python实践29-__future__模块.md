### 背景
在Python2.x代码中经常能看到使用__future__模块。那么__future__到底是做什么的呢？
1. > To avoid confusing existing tools that analyze import statements and expect to find the modules they’re importing.
2. > To ensure that future statements run under releases prior to 2.1 at least yield runtime exceptions (the import of __future__ will fail, because there was no module of that name prior to 2.1).
3. > To document when incompatible changes were introduced, and when they will be — or were — made mandatory. This is a form of executable documentation, and can be inspected programmatically via importing __future__ and examining its contents.

- 避免和现有分析import工具混淆，并得到你期望的模块
- 确保2.1之前的版本导入__future__产生运行时异常，因为2.1之前没有这个模块
- 文档化不兼容的改变，通常这些改变会在新版中强制执行。这类文档以可执行的形式组织，通过导入__future__进行可编程式的检查。

### Python2.x可用Python3.x的feature
- absolute_import： 绝对导入
- print_function：打印函数
- division：精确除法
- unicode_literals：unicode字面量

### divsion例子
- 2.x里面的除法/是地板除法，整数相除，结果仍是整数，余数会被扔掉
- 而在Python 3.x中，所有的除法都是精确除法，地板除用//表示
```
# output: 3，地板除
print(10/3)
```
vs
```
from __future__ import division

# output: 3.333333333
print(10/3)

# output: 3，地板除
print(10//3)
```

### unicode例子
- 2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，而在3.x中，所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的
- 而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。
```
# False
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# True
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# True
print '\'xxx\' is str?', isinstance('xxx', str)
# True
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
```
vs
```
from __future__ import unicode_literals

# True
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# True
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# False
print '\'xxx\' is str?', isinstance('xxx', str)
# True
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/lib/future/20180128)

如果觉得本文对您有帮助，敬请点赞。