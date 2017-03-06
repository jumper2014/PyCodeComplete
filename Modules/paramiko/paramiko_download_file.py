# coding=utf-8
# 从远程下载文件

import paramiko

t = paramiko.Transport(("192.168.1.211", 22))
t.connect(username="admin", password="123456")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = '/tmp/test.txt'
localpath = 'E:/test.txt'
sftp.get(remotepath, localpath)
t.close()
