#!/usr/bin/env python
# coding=utf-8
"""
准备：远程主机已经可以让本机免密码登陆
本机使用 paramiko 控制远程主机
本机使用 paramiko 上传文件到远程主机
Python 2.7运行通过
"""

import paramiko

if __name__ == "__main__":
    remote_host = '192.168.253.157'
    ssh_port = 22
    user_name = 'root'

    # 加载RSA私钥
    private_key_file = '/root/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_key_file)

    # 远程执行命令
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    # 使用私钥连接远程主机
    s.connect(remote_host, ssh_port, user_name, pkey=key)

    std_in, std_out, std_err = s.exec_command('ifconfig')
    print std_out.read()
    s.close()

    # 上传文件到远程主机
    t = paramiko.Transport((remote_host, ssh_port))
    t.connect(username=user_name, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    # 上传当前目录下的文件到远程主机的/root/目录下
    # 也可以直接指定绝对路径
    sftp.put("test.txt", "test.txt")
    t.close()

