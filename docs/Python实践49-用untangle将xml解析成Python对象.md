### untangle简介
- untangle是一个简单的xml解析库，能够把xml转换成python对象
- 同一个名字的兄弟元素组成数组
- 通过parent.child访问子元素，通过element['attribute']访问属性
- 使用parse()方法处理xml文件，URL或者是xml字符串
- 支持Python 2.6, 2.7, 3.3, 3.4, 3.5, 3.6 和 pypy

### 局限
- 要访问的xml元素标签不能是Python关键字，例如and
- 使用下划线_来替换-, . 和 :等特殊字符，例如 <foobar><foo-bar/></foobar> 可以通过foobar.foo_bar来访问

### 举个栗子
```
xml_str = '''
        <mydocument has="an attribute">
            <and>
                <many>elements</many>
                <many>more elements</many>
            </and>
            <plus a="complex">elements</plus>
            <plus a="simple">element as well</plus>
        </mydocument>
    '''
    obj = untangle.parse(xml_str)   # 解析字符串形式XML
    print(obj.mydocument['has'])    # 访问属性 an attribute
    print(obj.mydocument.plus[1].cdata)     # 访问文本 element as well
    # print(obj.mydocument.and)       # 报错，无法处理Python关键字
```

### 代码下载
本文内容和代码已经归档到https://github.com/jumper2014/PyCodeComplete，欢迎star