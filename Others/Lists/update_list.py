# coding=utf-8

name_list = ['python', 'perl', 'java']

# 删除尾部元素
print name_list.pop()
print name_list

# 增加元素，append方法
name_list.append('test append')
print name_list

# 增加元素，在指定位置插入， insert方法
name_list.insert(1, 100)
print name_list

# 删除元素，删除指定位置的元素
print name_list.pop(0)
print name_list

# 删除元素，删除指定值的元素
name_list.remove(100)
print name_list

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
