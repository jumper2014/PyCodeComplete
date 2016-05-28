# coding=utf-8
# 上传文件到远程

import paramiko

t = paramiko.Transport(("192.168.1.211", 22))
t.connect(username="admin", password="123456")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = '/tmp/test.txt'
localpath = 'D:/test.txt'
sftp.put(localpath,remotepath)
t.close()
