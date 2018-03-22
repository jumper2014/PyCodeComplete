#!/usr/bin/env python
# coding=utf-8
# 读取ini配置文件

import configparser


def parse(config_file_path):
    cfp = configparser.ConfigParser()
    cfp.read(config_file_path)

    # 获得section
    s = cfp.sections()
    print('sections: ', s)

    # 获得某section下面的选项
    o = cfp.options('baseconf')
    print('options: ', o)

    # 获得某section下面的选项和配置
    v = cfp.items('baseconf')
    print('db: ', v)

    # 获得某section下面的单个选项和配置
    db_host = cfp.get('baseconf', 'host')
    print(db_host)  # 127.0.0.1

    # 修改并保存
    cfp.set('baseconf', 'host', '192.168.0.1')
    cfp.write(open('db_config.ini', 'w'))


if __name__ == "__main__":
    parse("db_config.ini")