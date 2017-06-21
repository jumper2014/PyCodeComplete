# coding=utf-8

import json

dict1 = {'name': 'wuya', 'age': 22, 'address': 'xian'}

print u'未序列化前的数据类型为:', type(dict1)
print u'未序列化前的数据:', dict1

# 对dict1进行序列化的处理
str1 = json.dumps(dict1)
print u'序列化后的数据类型为:', type(str1)
print u'序列化后的数据为:', str1

# 对str1进行反序列化
dict2 = json.loads(str1)
print u'反序列化后的数据类型:', type(dict2)
print u'反序列化后的数据：', dict2
