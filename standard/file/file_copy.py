# coding=utf-8
# 复制文件

import shutil
import os

shutil.copy("file_copy.py", "file_copy.py.bak")
print "file_copy.py" in os.listdir(os.curdir)
print "file_copy.py.bak" in os.listdir(os.curdir)
