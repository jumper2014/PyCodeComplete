# coding=utf-8
import os.path

print os.path.isfile('/etc/passwd')
print os.path.isfile('/etc')
print os.path.isfile('/does/not/exists')

# for both dir and file
print os.path.exists('/etc/passwd')
print os.path.exists('/etc')
print os.path.exists('/does/not/exists')