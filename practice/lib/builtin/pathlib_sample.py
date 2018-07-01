#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from pathlib import Path

print(Path.home())  # 用户目录
cwd = Path.cwd()    # 当前目录
print(cwd)

full_name = Path(__file__)   # 当前文件名
print(full_name)
print(full_name.suffix)     # 文件后缀
print(full_name.stem)   # 文件名不带后缀
print(full_name.name)   # 带后缀的完整文件名
print(full_name.parent)     # 路径的上级目录
print(full_name.is_dir())   # 判断是否是目录
print(full_name.resolve())  # 返回绝对路径
print(full_name.exists())       # 路径是否存在
print(full_name.root)       # 返回路径的根目录
print(full_name.parts)  # 分割路径 类似os.path.split(), 不过返回元组
print(full_name.stat())     # 返回路径信息, 同os.stat()
