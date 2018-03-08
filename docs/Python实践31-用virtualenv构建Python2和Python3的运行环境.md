### 什么是VirtualEnv
> - virtualenv is a tool to create isolated Python environments.
> - The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you install everything into /usr/lib/python2.7/site-packages (or whatever your platform’s standard location is), it’s easy to end up in a situation where you unintentionally upgrade an application that shouldn’t be upgraded.
- virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境
- 典型的一种场景就是你的机器上同时需要运行Python2和Python3两个版本的Python，那么用virtualenv可以非常方便地管理不同版本的Python
- 当然，更多的时候virtualenv也被用来创建同一Python版本+不同版本第三方库的运行环境。

### 安装virtualenv
pip install virtualenv

### CentOS 7上安装Python3
- yum install epel-release
- 或者 wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
- yum install python34
- 检查安装 $ python3
- 升级刚刚安装的virtualenv: pip install --upgrade virtualenv (here was a bug in the OP's version of virtualenv, so we run this command to fix it)


### 创建两套Python运行环境
#### 创建Python2的环境
- virtualenv env2x     # 使用Python2创建环境
- cd env2x
- source ./bin/activate # 进入
- 使用你的python2环境
- deactivate   # 退出

#### 创建Python3的环境
- virtualenv –p python3 env3x # 使用Python3创建环境
- cd env3x
- source ./bin/activate # 进入
- 使用你的python3环境
- deactivate   # 退出


### 原理
virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。


如果觉得本文对您有帮助，敬请点赞。