# coding=utf-8
# 移动文件

import shutil
import os

os.renames("file_copy.py", "../file_copy.py")
os.renames("../file_copy.py", "file_copy.py")
