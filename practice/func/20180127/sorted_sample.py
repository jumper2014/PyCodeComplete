#!/usr/bin/env python
# coding=utf-8
# 演示sorted()里面使用cmp，key进行比较排序


def my_cmp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


students = [('li', 22), ('zhang', 25), ('wang', 21), ('chen', 20)]
sorted_students = sorted(students, cmp=lambda x, y: my_cmp(x[1], y[1]))
# 其实等价于下面这句，用cmp()代替自定义的my_cmp()
# sorted_students = sorted(students, cmp=lambda x, y: cmp(x[1], y[1]))
print(sorted_students)

# 按照tuple里面的第二个元素，也就是年龄排序
key_sorted_students = sorted(students, key=lambda x: x[1])
print(key_sorted_students)