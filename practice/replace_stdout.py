# coding=utf-8
import sys

# 重定向stdout到一个文件
sys.stdout = open("stdout.log", "w")
print("hello world")

# 重置stdout
reload(sys)
print("hello again")