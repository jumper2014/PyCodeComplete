#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import requests

if __name__ == '__main__':
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
