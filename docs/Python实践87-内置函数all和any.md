### 内置函数all
- 接收一个可迭代对象，如果其中所有的元素都是True，或者该可迭代对象中没有元素，返回True
- 等价于
```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

### 内置函数any
- 接收一个可迭代对象，如果其中有元素是True，返回True。如果该可迭代对象中没有元素，返回Flase
- 等价于
```
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

### 实例
```
if __name__ == "__main__":
    elements = [False, False, True]
    print(all(elements))  # False
    print(any(elements))  # True

    elements = []
    print(all(elements))  # True
    print(any(elements))  # False
```