### 为何需要使用代理
- 很多网站如果发现同一个IP发出的大量请求，就会封禁这样的IP
- 爬虫为了避免被封IP，必须不断地更换IP地址发出请求，这个时候就需要使用代理


### 使用httpbin来确认已使用代理
- httpbin是大神Kenneth Reitz的一个开源项目，提供免费的HTTP请求和响应服务
- 向http://httpbin.org/ip发起get请求，将会返回发起请求的IP地址
- 如果使用代理向http://httpbin.org/ip发起get请求，就会返回代理的IP地址


### requests库的代理参数
- requests库有一个代理参数proxies可以指定通过代理服务器发起请求
- proxies参数是一个字典，里面包含了http和https的代理URL


### 举个栗子
```
    # 不使用代理
    resp = requests.get('http://httpbin.org/ip')
    print(resp.text)
    # {"origin": "114.93.163.248"}

    proxies = {
        'http': 'http://139.227.252.141:8118',
        'https': 'https://139.227.252.141:8118'
    }

    # 使用代理
    resp = requests.get('http://httpbin.org/ip', proxies=proxies)
    print(resp.text)
    # {"origin": "139.227.252.141"}
```