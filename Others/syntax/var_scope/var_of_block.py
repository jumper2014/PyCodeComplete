# coding=utf-8

# 块级作用域

# 代码执行成功，没有问题；在Java/C#中，执行上面的代码会提示name，age没有定义，
# 而在Python中可以执行成功，这是因为在Python中是没有块级作用域的，
# 代码块里的变量，外部可以调用，所以可运行成功；

if 1 == 1:
    name = "lzl"

print(name)


for i in range(10):
    age = i

print(age)
