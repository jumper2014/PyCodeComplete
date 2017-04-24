# coding=utf-8

import subprocess

# 不转义
subprocess.call(['echo', 'l'])

# 转义
subprocess.call('echo %PATH%', shell=True)

# 获取输出
result = subprocess.check_output('echo %PATH%', shell=True)
print result
