# coding=utf-8
# author: Zeng YueTian


import os

# os.system("python system_test.py")

os.system("nohup python system_test.py > /dev/null 2>&1 &")
print "done"