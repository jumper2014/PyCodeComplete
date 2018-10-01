### 使用@property
- 使用getter和setter方法来控制类的成员变量访问，编写出的代码不Pythonic
- 使用Python内置的@property装饰器可以相对优雅地把一个方法变成属性调用
- 使用@property来将getter方法变成属性，此时@property本身又创建另外一个装饰器@<属性名>.setter，负责将setter方法变成属性赋值
- 如果只定义了@property，未定义@<属性名>.setter，那么这就是一个只读属性

### 举个栗子
```
class User(object):
    def __init__(self, name):
        self.name = name
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 100 or value < 0:
            self._age = 0
        else:
            self._age = value


if __name__ == '__main__':
    user = User('Li')
    user.age = 101
    print(user.age)     # 0
```