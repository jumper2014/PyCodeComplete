### 背景
- 今天花了一些时间，过了一下这几年自己用Python开发的自动化测试框架，然后将其中常用到Python库抽出来，简单整理了一下它们的用处。
- 只要掌握了这些常用的Python库，足以应对大多数自动化测试框架和工具的开发工作。
- 为了从若干源代码文件中找出这些被引用的Python库，还专门写了一个小工具来查找它们，该工具已经上传到github,地址是：import_search.py


### 基本库：
- sys 程序和Python解析器的交互
- os 启动新进程；操作文件和目录
- re  正则表达式，字符串匹配
- string 基本字符串操作
- inspect 提供自省和反射功能
- importlib 支持动态导入
- bitstring二进制数据处理
- zipfile 压缩解压文件
- tarfile 压缩解压文件
- random 随机数，概率
- uuid 生成唯一码
- defaultdict  带默认值的字典
- fcntl 操作文件描述符
- signal  信号处理
- threading  线程库，构建并发应用
- psutil 系统性能参数

### 命令行，读取配置：
- optparse 处理命令行选项
- glob 文件路径查找
- yaml 访问yaml数据文件
- ConfigParser 读取配置文件
- xml XML库
- pickle 序列化
- json 序列化

### 网络请求相关：
- libxml2  XML解析器
- urlparse URL解析
- urllib 访问URL资源
- urllib2 访问URL资源
- cookielib http客户端的cookie处理
- requests 神器，用于发送网络请求，常用于接口测试
- httplib http请求客户端
- BeautifulSoup 从HTML或XML文件中提取数据的Python库

### 网络数据包：
- scapy 网络嗅探工具包
- dpkt 网络数据报解析
- pcapy 解析pcap文件
- socket TCP,UDP数据协议
- struct 将python基本类型值与用python字符串格式表示的C struct类型间的转化，主要用于网络数据传输

### 测试系统构建：
- flask  构建web应用，构建HTTP接口 
- tornado 构建web应用，构建HTTP接口
- BaseHTTPServer 简单HTTP服务器
- appium App自动化测试工具
- selenium 大名鼎鼎的web自动化测试工具
- behave BDD自动化测试框（通用自动化测试框架）
- unittest  Python内置自动化测试框架（通用自动化测试框架）
- logging  日志库
- traceback 调试信息
- nanotime  纳秒级的时间
- time 时间访问和转换函数
- datetime  日期和时间
- jenkinsapi 访问jenkins

### 分布式系统构建：
- xmlrpclib  基于xml的远程RPC库
- fabric  利用ssh高效部署和管理系统的工具，用于远程执行命令和部署文件
- paramiko 遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接。用于远程执行命令和部署文件

### 大数据和数据库相关：
- avro avro是一个数据序列化系统
- etcd etcd访问库
- pyspark spark库
- hdfs  hdfs库
- pyhive hive库
- redis 访问redis数据库
- rediscluster 访问redis集群
- pymongo 访问mongodb
- kafka 访问kafka
- pykafka 访问kafka
- sqlalchemy ORM库
- MySQLdb 访问MySQL数据库

### 结果展示：
- smtplib 负责发送邮件
- email  负责构造邮件
- numpy 数据处理
- math 顾名思义
- matplotlib 数据绘图包
- pylab 绘制二维,三维数据
- pychart 制作图表

### 代码下载

本文code已经归档到github，您可以访问下面的链接获得。欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/tool)  


