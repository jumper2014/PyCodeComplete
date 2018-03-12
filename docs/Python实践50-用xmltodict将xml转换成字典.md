### 什么是xmltodict
- xmltodict是另外一个用于处理xml的简易的Python库
- xmltodict致力于将xml变得像json一样
- xmltodict支持将xml转成字典或者转回xml

### 用代码说话
假如我们的file.xml文件内容如下：
```
<mydocument has="an attribute">
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex">
    element as well
  </plus>
</mydocument>
```
我们可以用如下的方式来解析该xml文件
```
# 将xml读出
    with open('file.xml') as fd:
        doc = xmltodict.parse(fd.read())
        print(doc['mydocument']['@has'])  # == u'an attribute'
        print(doc['mydocument']['and']['many'])  # == [u'elements', u'more elements']
        print(doc['mydocument']['plus']['@a'])  # == u'complex'
        print(doc['mydocument']['plus']['#text'])  # == u'element as well'

    # 将字典转换成xml
    with open('out.xml', 'w') as f:
        mydict = {
            'text': {
                '@color': 'red',
                '@stroke': '2',
                '#text': 'This is a test'
            }
        }
        f.write(xmltodict.unparse(mydict))
        """ 生成的xml文件结果如下
        <?xml version="1.0" encoding="utf-8"?>
        <text stroke="2" color="red">This is a test</text>
        """
```

### 代码下载
本文内容和代码已经归档到https://github.com/jumper2014/PyCodeComplete，欢迎star