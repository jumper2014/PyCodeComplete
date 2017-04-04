# coding=utf-8
# 在函数中使用全局变量

globvar = 0


def set_globvar_to_one():
    global globvar # 需要用global修饰一下
    globvar = 1


def print_globvar():
    print globvar  # 如果只是读的话,不用global修饰


set_globvar_to_one()
print_globvar()



