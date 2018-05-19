### assert简介
- 形式：assert condition, your message
- condition为True时，程序继续运行，下一个语句会被执行
- condition为False时将会抛出AssertionError异常，该异常的信息为your message
- assert常常用来调试和测试

### 简单的例子
```
def divide(num1, num2):
    assert num2 != 0, "Divisor cannot be zero"
    return num1 / num2


if __name__ == '__main__':
    try:
        a2 = divide(12, 0)
    except AssertionError as e:
        print(e)
    # Divisor cannot be zero

```