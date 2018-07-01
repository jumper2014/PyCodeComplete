### pprint简介
- pprint是python的一个打印模块，可以用比print优雅的格式打印数据
- pprint不是万能的，无法使每个人都满意
- pprint使用不同的参数来控制打印格式，有的时候为了好看，需要针对不同的数据使用不同的参数

### pprint的主要参数
-  indent --- 缩进
-  width --- 一行最大宽度
-  depth --- 打印的深度，这个主要是针对一些可递归的对象，如果超出指定depth，其余的用"..."代替
-  stream ---指输出流对象，如果stream=None，那么输出流对象默认是sys.stdout

### 举个栗子
```
if __name__ == '__main__':
    import pprint

    data = (
        "this is a string",
        [1, 2, 3, 4, {"name": "python", "age": 30}],
        ("more tuples", 1.0, 2.3, 4.5),
        "this is yet another string"
    )

    pprint.pprint(data, indent=4, width=20, depth=2)
```
- 结果如下，注意由于其中字典的内容是第3层，超过了depth=2，所以会在结果中展示...
```
(   'this is a '
    'string',
    [   1,
        2,
        3,
        4,
        {...}],
    (   'more '
        'tuples',
        1.0,
        2.3,
        4.5),
    'this is yet '
    'another '
    'string')
```
