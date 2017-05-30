# coding=utf-8

"""
__author__ = 'zengyuetian'
precondition: pip install redis
modified by dh 2015.08.11
"""

import redis

REDIS_IP = "192.168.253.136"
REDIS_PORT = 6379


class RedisDB(object):
    def __init__(self, host='127.0.0.1', port=6379, db=0):
        self.db = redis.Redis(host=host, port=port, db=db)

    def shutdown(self):
        self.db.shutdown()

    def select_db(self, db):
        self.db.select(db)

    def remove_db(self, db):
        self.db.move(db)

    def set(self, key, value):
        self.db.set(key, value)

    def get(self, key):
        return self.db.get(key)

    def get_keys(self):
        return self.db.keys()

    def llen(self, key):
        return self.db.llen(key)


if __name__ == "__main__":
    db = RedisDB(REDIS_IP, REDIS_PORT)
    print db.get_keys()
