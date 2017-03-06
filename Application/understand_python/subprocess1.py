# coding=utf-8
# author: Zeng YueTian

import subprocess

# Popen启动进程
proc = subprocess.Popen(['echo', 'hello from the child'], stdout=subprocess.PIPE)

# communicate 用于读取子进程的输出
out, err = proc.communicate()

print(out.decode('utf-8'))

