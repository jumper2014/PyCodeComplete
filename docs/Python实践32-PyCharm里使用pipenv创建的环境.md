### 什么是pipenv
- 详细内容请参考董伟明的文章[《使用pipenv管理你的项目》](https://zhuanlan.zhihu.com/p/32913361)
- pipenv 是 Pipfile 主要倡导者、requests 作者 Kenneth Reitz 写的一个命令行工具，主要包含了Pipfile、pip、click、requests和virtualenv。Pipfile和pipenv本来都是Kenneth Reitz的个人项目，后来贡献给了pypa组织。Pipfile是社区拟定的依赖管理文件，用于替代过于简陋的 requirements.txt 文件。
- pipenv自动关联项目相关的virtualenv，能够快速的加载virtualenv。
- pipenv提供的pipenv替代pip并自带一个依赖清单Pipfile，和依赖锁定Pipfile.lock，可以卸载依赖。
- pipenv兼容Python 2/3


### Mac下安装pipenv
- brew install python3  # 如果已经安装了可以忽略
- python3 -m pip install --upgrade --force-reinstall pip
- pip3 install pipenv --user  # 推荐安装在个人目录下
- vim ~/.bash_profile加入下面的内容：export PATH="/Users/zyt/Library/Python/3.6/bin:$PATH"
- source ~/.bash_profile

### 创建项目目录
- mkdir new
- cd new
- pipenv install (耐心等待)
- pipenv shell               # 进入新环境
> Shell for /Users/zyt/.local/share/virtualenvs/new-cRH-55u9 already activated.
- pipenv install requests    # 安装第三方包
- exit                       # 退出


### 配置PyCharm使用pipenv环境
- 启动PyCharm，打开名称为new的项目
- 进入项目设置，搜索Project Interpreter
- 在Project Interpreter的右上角配置按钮上选择Add Local
- 选择VirtualEnv Environment
- 复制刚才的环境路径"/Users/zyt/.local/share/virtualenvs/new-cRH-55u9/bin/python"到粘贴板，粘贴到existing environment的interpreter下面，点击确定。
- 这样，你就可以在PyCharm里用为new专门创建的python环境了。
