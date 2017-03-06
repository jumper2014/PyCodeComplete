# coding=utf-8
# 删除文件夹

import shutil
import os

# os.removedirs 不能删除非空文件夹
try:
    os.removedirs("test_dir")
except Exception as msg:
    print msg

# 使用 shutil.rmtree 来删除非空文件夹
shutil.rmtree("test_dir")