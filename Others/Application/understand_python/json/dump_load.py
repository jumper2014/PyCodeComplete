# coding=utf-8

import json

fname = "json.log"

list1 = ['selenium', 'appium', 'android', 'ios', 'uiautomator']

# 把list1先序列化,再写入到一个文件中
print json.dump(list1, open(fname, 'w'))
print u'文件内容为:'
r = open(fname, 'r+')
print r.read()

# 先读取文件内容，再进行反序列化
res = json.load(open(fname, 'r+'))
print res, u'数据类型:', type(res)
