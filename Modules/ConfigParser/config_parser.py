# coding=utf-8
# 读取ini配置文件

import ConfigParser


def parse(config_file_path):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)

    s = cf.sections()
    print 'section: ', s

    o = cf.options('baseconf')
    print 'options: ', o

    v = cf.items('baseconf')
    print 'db: ', v

    db_host = cf.get('baseconf', 'host')
    print db_host


if __name__ == "__main__":
    parse("db_config.ini")