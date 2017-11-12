# coding=utf-8
# 题目,写一个函数,求两个整数之和,要求在函数体内,不得使用+,-,*,/四则运算符号


def add(num1, num2):
    while num2 != 0:
        num = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = num
        num2 = carry
    return num1

if __name__ == "__main__":
    assert add(123, 798) == 921
    assert add(111, 666) == 777

