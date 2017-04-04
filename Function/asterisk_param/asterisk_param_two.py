# coding=utf-8
# 函数定义和调用时用两个星号


def print_student_info1(**info):
    print("age:", info.get("age", None))
    print("score:", info.get("score", None))


def print_student_info2(age, score):
    print("age:", age)
    print("score:", score)


# 两个星号将会把字典完全unpack
info_dict = {"age": 20, "score": 99}
print_student_info1(**info_dict)
print_student_info2(**info_dict)
