# coding=utf-8
# count how many python file in this dir

import os

python_file_num = 0
for root, dirs, files in os.walk("."):
    for fi in files:
        # exclude init files
        if fi.find('.py') > -1 and fi.find('__init__.py') < 0:
            python_file_num += 1
            print(fi)

print("\nTotal python file number is {0}.".format(python_file_num))
