### 安装django
- mkdir web
- cd web
- pipenv install
- pipenv shell
- pip install Django
- 查看版本
```
$ python
>>> import django
>>> print(django.get_version())
2.0.5
```
- 或者用下面的方式查看版本
```
python -m django --version
2.0.5
```

### 基本命令
- 创建一个项目: django-admin startproject mysite
- 进入项目目录: cd mysite
- 启动服务器: python manage.py runserver
- 在指定端口启动服务器: python manage.py runserver 8080
- 支持通过本机所有IP访问: python manage.py runserver 0:8000
- 创建app: python manage.py startapp polls
- 根据项目设置自动创建数据库：python manage.py migrate
- 更新模型后创建migration: python manage.py makemigrations polls
- 用sqlmigrate查看migration的SQL语句：python manage.py sqlmigrate polls 0001
- migration检查：python manage.py check
- 应用migration：python manage.py migrate