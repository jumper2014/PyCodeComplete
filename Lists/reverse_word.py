# coding=utf-8
# 将字符串逐字或者逐词翻转



# 方案一  步长负一 实现翻转 最好的方法
my_str = '123'
print my_str
print my_str[::-1]


# 方案二 序列 翻转 需要有分割符
my_str = '1 2 3'
strs = my_str.split(' ')
strs.reverse()
print ' '.join(strs)


# 方案三 序列 翻转 API 需要配合join
my_str = '123'
print ''.join(reversed(my_str))  # reversed返回迭代器


#方案四 list的pop方法
#python3
my_str = '123'
for i in range(1,len(my_str)+1):
    print(list(my_str).pop())
