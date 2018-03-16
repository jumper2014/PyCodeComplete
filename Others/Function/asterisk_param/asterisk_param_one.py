# coding=utf-8
# 函数调用时，参数使用星号

# 星号作用于tuple/list/str前，意思是解包(unpack)tuple/list/str，
# 解包后的tuple/list/str将不再是一个参数，而是每个元素都是一个函数参数，依次传递给函数


def print_student_info(age, score):
    print("age:", age)
    print("score:", score)


info_list = [18, 100]
print_student_info(*info_list)

# 如果此时星号被作用于一个dict前，那么只有dict的key会被解包，然后作为参数传递
info_dict = {"age": 20, "score": 99}
print_student_info(*info_dict)
