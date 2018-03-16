# coding=utf-8
"""
操作MongoDB数据库的底层库

预先准备:
./mongo
use runoob
db.runoob.insert({age:1})
db.runoob.insert({age:2})
db.runoob.insert({age:3})
"""

from pymongo import MongoClient

MONGODB_HOST = "192.168.253.130"
MONGODB_PORT = 27017
DATABASE = "runoob"
COLLECTION = "runoob"


class MongoDB(object):
    def __init__(self, host=MONGODB_HOST, port=MONGODB_PORT):
        """
        建立连接
        :param host:mongo服务器地址
        :param port:mongo服务器端口
        :return:void
        """
        self.client = MongoClient(host, port)

    def get_all_collections(self, database):
        """
        获得一个数据库中的所有集合名称
        :param database: 数据库
        :return:集合名称列表
        """
        database = self.client[database]
        names = database.collection_names()
        return [str(name) for name in names]

    def get_one_doc(self, database, collection, condition=None):
        """
        返回满足条件的一条记录
        :param database:数据库
        :param collection:集合
        :param condition:查询条件，dict
        :return:dict
        """
        database = self.client[database]
        collection = database[collection]
        return collection.find_one(condition)

    def get_many_docs(self, database, collection, condition=None):
        """
        将满足条件的记录都返回
        :param database:
        :param collection:
        :param condition:
        :return:列表
        """
        database = self.client[database]
        collection = database[collection]
        result = []
        for item in collection.find(condition):
            result.append(item)
        return result

    def insert_one_doc(self, database, collection, documents):
        """
        插入一个document
        :param database:数据库
        :param collection:集合
        :param documents:文档，一个dict
        :return:void
        """
        # 选择库
        database = self.client[database]
        collection = database[collection]
        collection.insert_one(documents)

    def insert_multi_docs(self, database, collection, documents):
        """
        批量插入documents,插入一个数组
        :param database:数据库
        :param collection:集合
        :param documents:文档集合，dict的列表
        :return:void
        """
        database = self.client[database]
        collection = database[collection]
        collection.insert(documents)

    def clear_collection_datas(self, database, collection):
        """
        清空一个集合中的所有数据
        :param database:数据库
        :param collection:集合
        :return:void
        """
        database = self.client[database]
        collection = database[collection]
        collection.remove({})

    def delete_docs(self, database, collection, condition):
        """
        清空满足条件的数据
        :param database:数据库
        :param collection:集合
        :param condition:条件,dict
        :return:void
        """
        database = self.client[database]
        collection = database[collection]
        collection.remove(condition)


######################################
# for unit testing
######################################
if __name__ == "__main__":
    db = MongoDB()
    collectons = db.get_all_collections(DATABASE)
    print collectons

    cond = {"age": 1}
    doc = db.get_one_doc(DATABASE, COLLECTION, cond)
    print doc

    doc = {"age": 4}
    db.insert_one_doc(DATABASE, COLLECTION, doc)
    docs = db.get_many_docs(DATABASE, COLLECTION)
    print docs








    # data1 = {"peer_id": "0000000156BC45EE8F5AEA6A2866F111", "provinceId": 210000, "modifiedTime": "", "ip": "127.0.0.1",
    #          "version": "1.10.3", "lsmSize": 1111}
    # data2 = {"peer_id": "0000000156BC45EE8F5AEA6A2866F222", "provinceId": 210000, "modifiedTime": "", "ip": "127.0.0.1",
    #          "version": "1.10.3", "lsmSize": 1111}
    # # MongoDB.insert_one_doc("cdn_peer", "cdn_peer", data1)
    # # MongoDB.insert_multi_docs("cdn_peer", "cdn_peer", [data1, data2])
    # # print MongoDB.get_all_collections("cdn_peer")
    #
    # # MongoDB.get_one_doc("cdn_peer", "cdn_peer", {"provinceId": 210000})
    # print MongoDB.get_many_docs("cdn_peer", "cdn_peer", {"provinceId": 210000})
    # MongoDB.delete_docs("cdn_peer", "cdn_peer", {"provinceId": 210000})
    # print MongoDB.get_many_docs("cdn_peer", "cdn_peer", {"provinceId": 210000})
