# coding=utf-8

import etcd

# 创建etcd客户端对象，
# allow_redirect=True  这个参数是当断链的时候，etcd会再次复用connect创建可用的连接
client = etcd.Client(
    host="192.168.253.147",
    port=2379,
    allow_reconnect=True
)

client.read('/nodes/n2').value

#recursive递归的目录
#sorted 排序
r = client.read('/nodes', recursive=True, sorted=True)
for child in r.children:
    print("%s: %s" % (child.key,child.value))

#相当于zookeeper的watch监听
client.read('/nodes/n2', wait=True) #Waits for a change in value in the key before returning.
client.read('/nodes/n2', wait=True, waitIndex=10)