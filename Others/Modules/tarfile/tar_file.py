# coding=utf-8
"""
压缩和解压*.tar.gz文件

"""

import tarfile
import os

def untar(filename, dir):
    t = tarfile.open(filename)
    t.extractall(path = dir)



def tar(filename):
    t = tarfile.open(filename + ".tar.gz", "w:gz")
    for root, dir, files in os.walk(filename):
        print root, dir, files
        for file in files:
            full_path = os.path.join(root, file)
            t.add(full_path)
    t.close()
