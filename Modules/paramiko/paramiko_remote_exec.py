# coding=utf-8
# 执行远程命令

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.64", 22, "admin", "123456")
stdin, stdout, stderr = ssh.exec_command("ls /")
print stdout.readlines()
ssh.close()

