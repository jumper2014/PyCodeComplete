# coding=utf-8

import etcd

# 创建etcd客户端对象，
# allow_redirect=True  这个参数是当断链的时候，etcd会再次复用connect创建可用的连接
client = etcd.Client(
    host="192.168.253.147",
    port=2379,
    allow_reconnect=True
)

client.write('/nodes/n1', 1, ttl=100)
client.write('/nodes/n2', 2, ttl=400)

# create only
client.write('/nodes/n3', 'test', preExist=False)

client.write('/nodes/n3', 'test2', preValue='test1')

# mkdir
client.write('/nodes/queue', None, dir=True, preExist=False)

# Append a value to a queue dir
client.write('/nodes/queue', 'test', append=True) # will write i.e. /nodes/queue/11
client.write('/nodes/queue', 'test2', append=True) # will write i.e. /nodes/queue/12


