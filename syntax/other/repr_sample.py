# coding=utf-8
# repr函数用来取得对象的规范字符串表示

# 反引号（也称转换符）可以完成相同的功能。
# 在大多数时候有eval(repr(object)) == object


i = []
i.append('item')

print `i`       # "['item']"

print repr(i)  # "['item']"
