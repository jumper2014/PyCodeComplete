### demjson简介
- 在Python有内置json库之前就开始开发了
- 曾经的版本最低能支持Python2.3
- demjson2.0以后最低能支持Python2.6
- demjson在非strict模式下能解析不规范的json串，这在某些情况下非常有用
- demjson在strict模式下能够报告不规范json串的具体错误
- 自动处理很多额外的Python数据类型

### 举个栗子
```
    # From Python to JSON
    print(demjson.encode(['one', 42, True, None]))
    # '["one",42,true,null]'

    # From JSON to Python
    print(demjson.decode('["one",42,true,null]'))
    # ['one', 42, True, None]

    # 处理不规范的JSON字符串
    print(demjson.decode('{name: "python", age: 42}'))
    # {u'age': 42, u'name': u'python'}

    # 严格模式时，不规范的json串会报异常
    print(demjson.decode('{name: "python", age: 42}', strict=True))
    # demjson.JSONDecodeError
```

### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star