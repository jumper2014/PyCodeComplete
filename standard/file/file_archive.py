# coding=utf-8
# 压缩文件

import shutil

print shutil.get_archive_formats()

# 产生压缩文件
# shutil.make_archive(basename, format, root_dir)
shutil.make_archive("test_archive", "zip", "test_dir/")