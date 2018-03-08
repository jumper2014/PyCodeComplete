### 元类是什么
- 元类也叫metaclass
- 很多文章都说元类是类的类，理解起来更容易的下面的方式
- 对象是类的实例，类是元类的实例
- 在Python中除了type以外，都是对象，所以类也是对象，也可以被动态创建


### 关于type
- type()函数可以查看一个类型或变量的类型，例如User是一个class，User的类型就是type，而user是一个User实例，它的类型就是class User
- class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
- type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数动态创建出User类，而无需通过class User(object)...的定义，例如下面的两组代码等价：
```
class User(object):
    register = True


if __name__ == '__main__':
    user = User()
    print(user.register)
```
和
```
if __name__ == '__main__':
    User = type('User', (object,), dict(register=True))  # 创建User class
    user = User()
    print(user.register)
```
要创建一个class对象，type()函数依次传入3个参数：
- class的名称；
- 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
- class的成员绑定，这里我们把成员register绑定到True上。函数也同理。


### 使用元类动态创建类
- 除了使用type()动态创建类以外，还可以使用元类控制类的创建行为。
- 先定义一个用于创建目标类的元类，一般类名称带Metaclass。
- 例如我们可以先定义元类UserMetaclass，然后用UserMetaclass动态创建类User, 然后用User创建对象user
```
class UserMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['register'] = True
        return type.__new__(cls, name, bases, attrs)


class User(object):
    __metaclass__ = UserMetaclass


if __name__ == '__main__':
    user = User()
    print(user.register)
```
- 重点关注UserMetaclass的形式，`__new__`()方法接收到的参数依次是：
- 当前准备创建的类的对象；
- 类的名字；
- 类继承的父类集合；
- 类的成员集合。

### 什么时候使用元类
- python大师Tim Peters说过：元类是一种99%的人都不需要关心的深度魔法。当你在好奇你是否需要它，通常这就说明你并不需要（确切需要它的人不需要找任何原因解析为什么需要）。 
- 元类最主要的用处是类工厂，即生产类的工厂类，一个典型应用场景是实现ORM。
- 在简单的改变类时你可能并不想要使用元类。你能通过使用以下两种技术来改变类：monkey patching和 class decorators 


### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/runtime/20180228)