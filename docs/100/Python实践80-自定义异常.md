### 为什么要自定义异常
- 让代码可读性更好
- 为代码提供更加丰富的功能和信息

### 基类
- 一般我们自定义的异常可以使用Exception作为基类
- 自定义异常类的初始化函数记得要先调用基类的初始化函数

### 简单栗子
```
class VerifyException(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    user_age = -1
    try:
        if user_age < 0:
            raise VerifyException('User age is negative')
    except Exception as e:
        print(e.message)

```