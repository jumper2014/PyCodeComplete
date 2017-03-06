# coding=utf-8
# requests 模块号称 HTTP for Human

import requests

# r = requests.get("http://httpbin.org/get")
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")
#
# # 假如我们想访问 httpbin.org/get?key=val
# payload = {'key': 'val'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)

# Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码。
r = requests.get('https://github.com/timeline.json')
print r.text

# 查看文字编码
print r.encoding

# 每次改变文字编码，text 的内容也随之变化
r.encoding = "ISO-8859-1"
print r.text

# Requests 中也有一个内置的 JSON 解码器处理 JSON 数据
print r.json()

# 状态码
print r.status_code

# 响应头
print r.headers['Content-Type']
