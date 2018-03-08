### 关于yaml
- YAML语言的设计目标，就是方便人类读写。如果你想要实现一些用ini不好做到的配置，可以使用yaml格式作为配置文件
- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格。
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可


### yaml数据结构
- YAML 支持的数据结构有三种。
- 对象
> - 键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
> - 对象的一组键值对，使用冒号结构表示。
- 数组
> - 一组按次序排列的值，又称为序列（sequence） / 列表（list）
> - 一组连词线开头的行，构成一个数组。
- 纯量（scalars）
> - 单个的、不可再分的值
> - 包括字符串，布尔值，整数，浮点数，Null，时间，日期

### 一个yaml文件
```
name: John Smith
age: 37
spouse:
    name: Jane Smith
    age: 25
children:
    -  name: Jimmy Smith
       age: 15
    -  name: Jenny Smith
       age: 12
```
和它对应的json文件如下：
```
{ name: 'John Smith',
  age: 37,
  spouse: { name: 'Jane Smith', age: 25 },
  children: 
   [ { name: 'Jimmy Smith', age: 15 },
     { name: 'Jenny Smith', age: 12 } ] 
}
```

### 读写yaml文件
```
import yaml

if __name__ == "__main__":
    with open('father.yml') as f:
        content = yaml.load(f)

        # output: <type 'dict'>
        print(type(content))
        print(content)

        content.update({'age': 38})
        print(content)

    with open('PyYAML.yml', 'w') as nf:
        yaml.dump(content, nf)
```
生成的新yaml文件形式如下：
```
age: 38
children:
- {age: 15, name: Jimmy Smith}
- {age: 12, name: Jenny Smith}
name: John Smith
spouse: {age: 25, name: Jane Smith}
```
仔细一看，跟原yaml文件不像嘛，尤其是几个大括号，很刺眼，这可怎么办？

### 使用ruamel.yaml代替PyYAML
- 解决方法就是使用ruamel.yaml代替PyYAML，因为PyYAML貌似已经不再维护了
- 安装：pip install ruamel.yaml
- 使用ruamel.yaml库里面函数参数Loader=ruamel.yaml.RoundTripLoader和Dumper=ruamel.yaml.RoundTripDumper可以用来保持新生成的yaml文件的表现和输入文件一致。代码如下：
```
from ruamel import yaml

if __name__ == "__main__":
    with open('father.yml') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)

        # output: <type 'dict'>
        print(type(content))
        print(content)

        content.update({'age': 38})
        print(content)

    with open('ruamel.yml', 'w') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)
```
生成新的yaml文件形式如下，正是我们期望的格式：
```
name: John Smith
age: 38
spouse:
  name: Jane Smith
  age: 25
children:
- name: Jimmy Smith
  age: 15
- name: Jenny Smith
  age: 12
```


### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/lib/yaml/20180131)

如果觉得本文对您有帮助，敬请点赞。