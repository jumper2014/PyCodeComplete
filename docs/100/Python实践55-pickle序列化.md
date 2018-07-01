### 什么是序列化
- 我们把变量从内存中变成可存储或传输的过程称之为序列化。
- 序列化在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思.
- 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
- 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

### Python的pickle模块
- pickle是python中独有的序列化模块，所谓独有，就是指不能和其他编程语言的序列化进行交互,因为pickle将数据对象转化为bytes
- dumps和dump都是进行序列化，而loads和load则是反序列化。
- dumps将所传入的变量的值序列化为一个bytes，然后，就可以将这个bytes写入磁盘或者进行传输
- 而dump则更加一步到位，在dump中可以传入两个参数，一个为需要序列化的变量，另一个为需要写入的文件。
- loads当我们要把bytes反序列化为内存对象
- 用load方法直接反序列化一个文件为内存对象


### pickle vs json
- 如果没有协同和交互的要求，那么就用pickle，直接序列化二进制数据就够用了，尤其是cPickle会给你带来高性能
- 如果有协同交互的要求，那么可以用json，它将生成可读的文本内容。比如在网络上传输。

### 一个例子
```
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print self.name + "_" + str(self.age)


# 序列化到文件
user = User("Python", 20)
user.show()
f = open('user.pkl', 'w')
pickle.dump(user, f)
f.close()

# 反序列化到内存
f = open('user.pkl', 'r')
user1 = pickle.load(f)
f.close()
user1.show()
```

### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star