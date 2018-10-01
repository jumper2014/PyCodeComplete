### configparser模块
- 该模块在Python2中叫ConfigParser
- 在python3中模块名修改为configparser
- 该模块的作用 就是使用模块中的RawConfigParser()，ConfigParser()，SafeConfigParser()这三个方法（三者择其一），创建一个对象使用对象的方法对指定的配置文件做增删改查操作。


### 举个例子
- 例如配置文件db_config.ini的内容如下：
```
[baseconf]
host = 127.0.0.1
port = 3306
user = root
db_name = api

[concurrent]
processor = 4
```
- 使用configparser来读写配置文件的代码如下：
```
import configparser


def parse(config_file_path):
    cfp = configparser.ConfigParser()
    cfp.read(config_file_path)

    # 获得section
    s = cfp.sections()
    print('sections: ', s)

    # 获得某section下面的选项
    o = cfp.options('baseconf')
    print('options: ', o)

    # 获得某section下面的选项和配置
    v = cfp.items('baseconf')
    print('db: ', v)

    # 获得某section下面的单个选项和配置
    db_host = cfp.get('baseconf', 'host')
    print(db_host)  # 127.0.0.1

    # 修改并保存
    cfp.set('baseconf', 'host', '192.168.0.1')
    cfp.write(open('db_config.ini', 'w'))


if __name__ == "__main__":
    parse("db_config.ini")
```

### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star
