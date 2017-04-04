# coding=utf-8

# 作用域链
# Python中有作用域链，变量会由内到外找，先去自己作用域去找，自己没有再去上级去找，直到找不到报错

name = "lzl"


def f1():
    name = "Eric"

    def f2():
        name = "Snor"
        print(name)

    f2()


f1()
