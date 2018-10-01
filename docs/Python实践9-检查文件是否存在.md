### 两种检查方式
- 一种是调用os.path模块中的方法isfile()
- 另一种是使用pathlib模块，在Python2中需要以第三方模块的方法安装，在Python3中pathlib是内置模块，无需安装
- 其实还可以直接使用open函数打开该文件，通过抛出的异常类型来判断文件是否存在，非常不建议使用这种方法。

### 实例展示
```
import os.path
import pathlib

# 检查给定路径是否是文件，能够区分文件和目录
print(os.path.isfile('/etc/passwd'))    # True
print(os.path.isfile('/etc'))           # False
print(os.path.isfile('/does/not/exists'))   # False

# 检查给定路径是否存在，无法能够区分文件和目录
print(os.path.exists('/etc/passwd'))    # True
print(os.path.exists('/etc'))           # True
print(os.path.exists('/does/not/exists'))   # False

# Python2需要安装pathlib, Python3中pathlib是内置模块，无需安装
path = pathlib.Path("/etc/passwd")
print(path.exists())                    # True
print(path.is_file())                   # True
print(path.is_dir())                    # False
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/lib/file/20180221)