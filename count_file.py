# coding=utf-8
#

import os

python_file_num = 0
for root, dirs, files in os.walk("."):
    for fi in files:
        if fi.find('.py') > -1:
            python_file_num += 1
            print(fi)

print(("\nTotal python file number is {0}.".format(python_file_num)))
