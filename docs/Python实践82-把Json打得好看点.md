### 背景
- 直接打印json数据，会打在一行，不利于查看
- json库的方法dumps其实提供一些参数，可以帮助格式化json串，这样打印出来的json数据会比较方便查看。

### 举个栗子
```
    import json
    your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    # 转换成Python对象
    parsed = json.loads(your_json)
    # 序列化成JSON并且打印
    print(json.dumps(parsed))
    """
    ["foo", {"bar": ["baz", null, 1.0, 2]}]
    """
    print(json.dumps(parsed, indent=4, sort_keys=True))
    """
    [
        "foo",
        {
            "bar": [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
    """
```