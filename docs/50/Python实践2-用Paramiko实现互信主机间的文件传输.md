### 背景
- Python的paramiko真乃神器也，不仅把需要用xmlrpclib实现的RPC功能非常简洁地实现了，还顺带着把用shell scp命令实现的文件传输也搞定了。我司测试在平时工作中，主要用它来部署文件和进行远程控制。由于都是在自己安装的机器，一般都是在paramiko脚本里指定用户名和密码连接远程机器，用起来十分方便。
- 但是有一天，突然接到紧急任务，需要在一个小时内，把测试环境部署到客户的一批机器上去用于演示，而客户的机器并不会给我们他们机器的用户名密码，仅仅是对我们的一台机器进行了授权，允许我们使用私钥登陆这批机器，也就是常说的免密码登陆。由于当时对paramiko不熟，没能搞明白如何让paramiko免密码进行文件传输，考虑到任务紧急，只好用scp的老方法部署文件，用是能凑合着用，但是心里一直不爽。
- 后来花了点时间，整理了一下如何在互信的主机间使用paramiko传输文件，供大家参考。（其实简单的要死）

### 解决问题
下面就请各位跟着我一步一步开始吧。  
- 准备两台主机，假设host1 ip：192.168.253.156， host2 ip：192.168.253.157
- 我们的目标是将host1上的文件分发到host2上去，文件为test.txt
- 首先，让host1能够免密码登陆host2。这里面需要3小步操作：
- 在host1上运行,  ssh-keygen -t   rsa，一路回车，这样会在你的用户root的目录下生成.ssh目录，里面包含了你root用户的公钥文件 id_rsa.pub和私钥文件 id_rsa
- 在host1上运行，ssh-copy-id   root@192.168.253.157，当需要确认时，输入yes，然后紧接着输入host2的root用户密码。这句命令将会将你的公钥内容复制到host2的受信任秘钥文件authorized_keys里去。当你使用host1的私钥登陆host2时，host2会使用authorized_keys里面存储的host1公钥来进行身份验证。  
- 在host1运行 ssh root@192.168.253.157,如果没有任何报错，就证明你已经可以让host1免密码登陆host2了。注意，这时你已经在host2上面登陆了，别忘了使用exit退出host2的登陆。
- 接着，在host1上面安装paramiko库，又是简单的要死，一句话:  pip install paramiko -y
- 然后创建一个Python文件paramiko_with_key.py，内容如下，主要语句的注释已经写好了，大家可以照葫芦画瓢试试。我上传到github的代码里面还有远程执行命令的功能，大家如果有需要可以去围观下。

```
import paramiko

if __name__ == "__main__":
    remote_host = '192.168.253.157'
    ssh_port = 22
    user_name = 'root'

    # 加载RSA私钥
    private_key_file = '/root/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_key_file)

    # 上传文件到远程主机
    t = paramiko.Transport((remote_host, ssh_port))
    t.connect(username=user_name, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    # 上传当前目录下的文件到远程主机的/root/目录下
    # 也可以直接指定绝对路径
    sftp.put("test.txt", "test.txt")
    t.close()
```

### 代码下载
地址如下：https://github.com/jumper2014/PyCodeComplete/
