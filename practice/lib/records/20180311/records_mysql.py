#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 演示用records操作MySQL

import records  # https://github.com/kennethreitz/records

datas = [
    {'name': 'Python', 'age': 20},
    {'name': 'Java', 'age': 25}
]

# records will create this db on disk if database doesn't exist already
db = records.Database('mysql://root:123456@localhost/practice')

db.query('DROP TABLE IF EXISTS user')
db.query('''CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT '',
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ''')

for user in datas:
    name = user['name']
    age = user['age']
    db.query('INSERT INTO user (name, age) VALUES(:name, :age)', name=name, age=age)

rows = db.query('SELECT * FROM user')
for row in rows:
    # 演示几种访问字段的方法
    print(row.id, row.name, row.age)
    print(row['id'], row['name'], row['age'])
    print(row[0], row[1], row[2])



