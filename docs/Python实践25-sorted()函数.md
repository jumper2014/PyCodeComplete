### 简介
- sorted()对可迭代对象进行排序，返回的是排序后的list
- sorted(iterable[, cmp[, key[, reverse]]])
- sorted()有三个可选参数，分别是cmp, key, reverse
- iterable -- 可迭代对象
- cmp -- 比较的函数，具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）

### cmp的例子
将学生信息按年龄排序
```
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
```

### key的例子
key指定一个接收一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认值为None。
```
# 按照tuple里面的第二个元素，也就是年龄排序
key_sorted_students = sorted(students, key=lambda x: x[1])
print(key_sorted_students)
```

### 代码下载
本文代码已经归档到github，您可以访问下面的链接获得，欢迎star该代码仓库。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/func/20180127)

如果觉得本文对您有帮助，敬请点赞。