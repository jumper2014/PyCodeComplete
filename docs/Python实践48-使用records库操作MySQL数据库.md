### records简介
- Records: SQL for Humans
- 大神kennethreitz开源的一个给人类用的数据库访问库
- 支持Python2.7和Python3
- 当前Python代码不超过600行
- 基于SQLAlchemy和Tablib开发
- 支持主流数据库RedShift, Postgres, MySQL, SQLite, Oracle, and MS-SQL


### records的特点
- 方便易用！！！
- 支持缓存查询的数据
- 支持从命令行导出数据
- 支持安全的参数化查询


### 管中窥豹
```
import records  
db = records.Database('mysql://root:123456@localhost/practice')
rows = db.query('SELECT * FROM user')
for row in rows:
    # 演示几种访问字段的方法
    print(row.id, row.name, row.age)
    print(row['id'], row['name'], row['age'])
    print(row[0], row[1], row[2])
```


### 代码下载
本文内容和代码已经归档到https://github.com/jumper2014/PyCodeComplete，欢迎star
