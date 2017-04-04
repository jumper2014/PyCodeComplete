# coding=utf-8
# 复制文件夹
import shutil
import os

shutil.copytree("test_dir/", "test_dir_copy/")

"test_dir_copy" in os.listdir(os.curdir)