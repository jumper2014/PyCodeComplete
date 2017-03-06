# coding=utf-8
# 访问字典中键值的两种方法

#对于一个字典(dict) d，除了可以用d['key']访问元素，也可以用d.get('key')。
# 当字典不包含某键值时，前一种方法会报异常，而后一种则会返回一个默认值，缺省的默认值是None。
# 下面代码展示这种用法：


info = {"name": "Python"}

print info.get("age", 32)
print info['age']
