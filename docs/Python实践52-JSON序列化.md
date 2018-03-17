### 什么是JSON
- JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
- JSON 是轻量级的文本数据交换格式
- JSON 独立于语言
- JSON 具有自我描述性，更易理解

### 什么是序列化
- 我们把变量从内存中变成可存储或传输的过程称之为序列化。
- 序列化在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思.
- 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
- 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。


### JSON序列化的优势
- 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML。
- 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
- JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
- 很多HTTP接口都采用JSON格式传输数据

### Python和JSON的数据类型对应关系
从Python到JSON
Python | JSON
---|---
dict |	object
list, tuple	| array
str, unicode |	string
int, long, float |	number
True |	true
False |	false
None |	null

从JSON到Python
JSON | Python
---|---
object | dict
array |	list
string | unicode
number (int) |	int, long
number (real) |	float
true |	True
false |	False
null |	None


### 举个栗子
- dumps, loads用于在Python对象和JSON字符串之间进行转换

```
user = {'id': 1, 'name': 'python', 'age': 30}
    print(type(user))   # < type 'dict' >
    print(user)         # {'age': 30, 'id': 1, 'name': 'python'}

    juser = json.dumps(user)
    print(type(juser))  # <type 'str'>
    print(juser)        # {"age": 30, "id": 1, "name": "python"}

    user2 = json.loads(juser)
    print(type(user2))  # <type 'dict'>
    print(user2)        # {u'age': 30, u'id': 1, u'name': u'python'}
```
- dump和load用于在Python对象和JSON文档之间进行转换
```
user = {'id': 1, 'name': 'python', 'age': 30}
    print(type(user))  # < type 'dict' >
    print(user)  # {'age': 30, 'id': 1, 'name': 'python'}

    json.dump(user, open('user.json', 'w'))

    fp = open('user.json', 'r')
    user2 = json.load(fp)
    print(type(user2))  # <type 'dict'>
    print(user2)  # {u'age': 30, u'id': 1, u'name': u'python'}
```

### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star