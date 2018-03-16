# coding=utf-8
# 将两个序列压在一起，形成一个元组的列表

name = ['java', 'python', 'perl']
age = [10, 11, 12]

print zip(name, age)  # [('java', 10), ('python', 11), ('perl', 12)]


#如果zip的两个序列长度不相等，zip之后的长度为短序列的长度
#另，zip obejct在python3中是generator-like的形式，不能直接打印，
#需转换为list
#!/usr/bin/env python3
#coding=utf-8

a = ['java', 'python', 'perl']
b = [1,2]

print(list(zip(a,b)))
print(list(zip(b,a)))

#[('java', 1), ('python', 2)]
#[(1, 'java'), (2, 'python')]

#在python3中才不能直接打印，python2中可以直接打印
#另，在python3中，zip object是generator-like形式，只能遍历一次
l1 = list(zip(a,b))
print(l1)
#结果为 [('java',1), ('python',2)]
print(l1)
#结果为 []

