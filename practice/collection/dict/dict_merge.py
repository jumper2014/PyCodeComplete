#!/usr/bin/env python
# coding=utf-8
# 合并字典


if __name__ == "__main__":
    # 定义两个有重复key的字典
    dict1 = {'usr': 'root', 'pwd': '123'}
    dict2 = {'ip': '192.168.1.1', 'usr': 'admin'}

    # 方法1
    # 获取字典的键值对的列表
    # 拼成一个新的列表
    # 将合并成的列表转变成新的字典
    # print(dict1.items())
    # print(dict2.items())
    # print(dict1.items() + dict2.items())
    dict3 = dict(dict1.items() + dict2.items())
    # output: {'ip': '192.168.1.1', 'pwd': '123', 'usr': 'admin'}
    print(dict3)

    # 方法2
    # 使用初始化函数
    dict4 = dict(dict1, **dict2)
    # output: {'ip': '192.168.1.1', 'pwd': '123', 'usr': 'admin'}
    print(dict4)

    # 方法3
    # 相同的key，后面的dict覆盖前面的dict
    dict2.update(dict1)
    # output: {'ip': '192.168.1.1', 'pwd': '123', 'usr': 'root'}
    print(dict2)
