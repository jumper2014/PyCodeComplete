### 背景
- 都说大城市的房价高，那最高价的房子多少钱一个平方呢？
- 都说python特别适合用来开发网络爬虫，那么不用现有的框架，自己应该如何开发一个爬虫呢？


### 自定义需求
- 开发一个链家网的爬虫，专门爬取城市中各小区的平均挂牌价格
- 爬取到的房价数据采用简单方便的方式存储在本地
- 这些房价数据能被用于简单的统计分析

### 设计
- 采用网络库采集链家网各大城市的小区房价数据
- 原始房价数据先存放到本地的csv文件中
- 对原始房价数据进行一定的清洗处理，存入关系数据库MySQL中
- 对原始房价数据进行一定的清洗处理，存入NoSQL数据库MongoDB中


### 链家网小区房价结构化数据分析
- 获得城市子域名代码，进入`http://<city>.lianjia.com`，例如sh-上海，bj-北京
- 获得该城市的小区栏目页面，`http://<city>.lianjia.com/xiaoqu/`
- 获得该城市的各区县页面，`http://<city>.lianjia.com/xiaoqu/<district>/`
- 获得该区县的各板块页面，`http://<city>.lianjia.com/xiaoqu/<area>/`
- 获得该板块的各小区信息页面，`http://<city>.lianjia.com/xiaoqu/<area>/pg<n>/`


### 具体实现
- 使用urllib2来访问链家网页面信息
- 使用beautifulsoup和lxml库解析页面信息
- 使用threadpool线程池库来调度完成爬取任务
- 使用records库来将数据写入MySQL
- 使用pymongo库来讲数据写入MongoDB


### 代码下载
- 该爬虫支持北京上海广州深圳等21个中国主要城市的小区房价数据的抓取，稳定可靠，速度嘛宇宙第二！
- 项目地址https://github.com/jumper2014/lianjia-spider，欢迎star