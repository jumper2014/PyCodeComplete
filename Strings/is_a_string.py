# coding=utf-8
# 判断一个值是否是字符串


def is_a_string(obj):
    return isinstance(obj, basestring)

print is_a_string(123456)  # False
print is_a_string(True)  # False
print is_a_string([1, 2, 3])  # False

print is_a_string("Hello Python")  # True
