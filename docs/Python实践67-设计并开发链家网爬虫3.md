### 数据清洗并入库
- 爬虫采集的数据存放在本地csv文件中，不方便进行统计分析
- csv文件中的数据是未经处理的原始内容，例如：20180401,杨浦,鞍山,和平花苑,76100元/m2,21套在售二手房
- 需要先进行数据清洗然后再入库，例如：20180401,杨浦,鞍山,和平花苑,76100,21

### 读取本地csv文件
- 提示用户需要入库哪个城市的数据
- 读取csv文件中该城市的房价数据
- 清洗数据，主要是对原始数据进行替换和删减，同时需要进行一些容错处理，比如某些字段里面有csv的分隔符逗号
```
# 清理数据
    count = 0
    for csv in files:
        with open(csv, 'r') as f:
            for line in f:
                count += 1
                text = line.strip()
                try:
                    # 如果小区名里面没有逗号，那么总共是6项
                    if text.count(',') == 5:
                        date, district, area, xiaoqu, price, sale = text.split(',')
                    elif text.count(',') < 5:
                        continue
                    else:
                        fields = text.split(',')
                        date = fields[0]
                        district = fields[1]
                        area = fields[2]
                        xiaoqu = ','.join(fields[3:-2])
                        price = fields[-2]
                        sale = fields[-1]
                except Exception as e:
                    print(text)
                    print(e.message)
                    continue
                sale = sale.replace(r'套在售二手房', '')
                price = price.replace(r'暂无', '0')
                price = price.replace(r'元/m2', '')
                price = int(price)
                sale = int(sale)
```

### 写入MySQL
- 使用records库，该库支持Python2和Python3
- 直接用raw sql进行插入操作
```
if database == "mysql":
    db.query('INSERT INTO xiaoqu (city, date, district, area, xiaoqu, price, sale) '
         'VALUES(:city, :date, :district, :area, :xiaoqu, :price, :sale)',
         city=city_ch, date=date, district=district, area=area, xiaoqu=xiaoqu, price=price, sale=sale)
```

### 写入MongoDB
- 使用pymongo库
- 直接用raw sql进行插入操作
```
elif database == "mongodb":
    data = dict(city=city_ch, date=date, district=district, area=area, xiaoqu=xiaoqu, price=price, sale=sale)
    collection.insert(data)
```

### 代码下载
- 该爬虫支持北京上海广州深圳等21个中国主要城市的小区房价数据的抓取，稳定可靠，速度嘛宇宙第二，同时支持Python2和Python3哦，还可以将数据存入MySQL和MongoDB中！
- 项目地址https://github.com/jumper2014/lianjia-spider，欢迎star