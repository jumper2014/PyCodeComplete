 ### `__call__`()
- Python里，函数式first-class对象，这表示，函数可以被传递给另外的函数或者方法，可以从子程序里返回，可以赋给变量。
- 类的实例也可以像函数一样被对待，比如将他们传递给其他的函数或者方法，并且被调用。想要达到这个目的，就要在类里专门定义__call__()方法。
- def `__call__`(self, [args ...]) 它接受一系列参数。假设x是类X的一个实例 , x.`__call__`(1, 2) 就等价于调用x(1,2)，而实例x仿佛就是一个函数。

### 使用场景
- `__call__`()的上述特性，可以允许开发者使用OO的方式来创建易用的API
- 当然使用闭包也能达到类似的效果，但是闭包不是那么易于理解。同时，当需要在多进程中传输数据时，面向对象的解决方法比闭包更可靠。

### callable()
- callable() 是一个bool函数，可以确定一个对象是否可以通过操作符()来调用，如果函数可以调用，返回True，否则返回False
- 注意类是callable的，因为调用类将会返回有一个新的实例。如果类的实例实现了`__call__`()方法，那么该实例也是callable的。

### 实例
下面的例子演示了如何使用类的`__call__`()方法来定义一组通用API，代码来自stackoverflow网站。
```
# filehash.py
import hashlib


class Hasher(object):
    """
    A wrapper around the hashlib hash algorithms that allows an entire file to
    be hashed in a chunked manner.
    """
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def __call__(self, file):
        hash = self.algorithm()
        with open(file, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), ''):
                hash.update(chunk)
        return hash.hexdigest()


md5    = Hasher(hashlib.md5)
sha1   = Hasher(hashlib.sha1)
sha224 = Hasher(hashlib.sha224)
sha256 = Hasher(hashlib.sha256)
sha384 = Hasher(hashlib.sha384)
sha512 = Hasher(hashlib.sha512)
```
下面是调用这些API
```
from filehash import sha1
print sha1('somefile.txt')
```


### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/class/20180123)

如果觉得本文对您有帮助，敬请点赞。
