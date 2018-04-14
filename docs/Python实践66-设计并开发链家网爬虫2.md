### 采集数据的主流程
- 让用户选择爬取哪个城市的房价数据
- 新建当日csv数据文件的存放目录
- 获得该城市各区县列表
- 获得各区县的版块列表
- 获得各版块的小区列表
- 每个版块的房价数据爬取作为一个任务
- 创建线程池，将所有的爬取任务交给线程池执行
- 统计一共爬取了多少小区数据，花费了多少时间

### 具体实现
#### 线程池的主要代码结构
```
# 针对每个板块写一个文件,启动一个线程来操作
pool_size = 50
pool = threadpool.ThreadPool(pool_size)
requests = threadpool.makeRequests(collect_xiaoqu_data, args)
[pool.putRequest(req) for req in requests]
pool.wait()
pool.dismissWorkers(pool_size, do_join=True)        # 完成后退出
```

#### 获取版块下小区房价数据
- 首先进入版块小区列表页
- 如果有总页数的element，那么获得总页数
- 如果没有总页数的element，那么总页数是1
- 遍历这些列表页，获得各小区信息
```
def get_xiaoqu_info(city, area):
    district = area_dict.get(area, "")
    chinese_district = get_chinese_district(district)
    chinese_area = chinese_area_dict.get(area, "")
    xiaoqu_list = list()
    page = 'http://{0}.lianjia.com/xiaoqu/{1}/'.format(city, area)
    print(page)

    response = requests.get(page, timeout=10)
    html = response.content
    soup = BeautifulSoup(html, "lxml")

    # 获得总的页数
    try:
        page_box = soup.find_all('div', class_='page-box')[0]
        matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
        total_page = int(matches.group(1))
    except Exception as e:
        print("\tWarning: only find one page for {0}".format(area))
        print("\t" + e.message)
        total_page = 1

    # 从第一页开始,一直遍历到最后一页
    for i in range(1, total_page + 1):
        page = 'http://{0}.lianjia.com/xiaoqu/{1}/pg{2}'.format(city, area, i)
        response = requests.get(page, timeout=10)
        html = response.content
        soup = BeautifulSoup(html, "lxml")

        # 获得有小区信息的panel
        house_elems = soup.find_all('li', class_="xiaoquListItem")
        for house_elem in house_elems:
            price = house_elem.find('div', class_="totalPrice")
            name = house_elem.find('div', class_='title')
            on_sale = house_elem.find('div', class_="xiaoquListItemSellCount")

            # 继续清理数据
            price = price.text.strip()
            name = name.text.replace("\n", "")
            on_sale = on_sale.text.replace("\n", "").strip()

            # 作为对象保存
            xiaoqu = XiaoQu(chinese_district, chinese_area, name, price, on_sale)
            xiaoqu_list.append(xiaoqu)
    return xiaoqu_list
```

### 代码下载
- 该爬虫支持北京上海广州深圳等21个中国主要城市的小区房价数据的抓取，稳定可靠，速度嘛宇宙第二，同时支持Python2和Python3哦，还可以将数据存入MySQL和MongoDB中！
- 项目地址https://github.com/jumper2014/lianjia-spider，欢迎star