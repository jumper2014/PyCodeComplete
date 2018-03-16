from socket import *
from time import ctime

HOST = ''
PORT = 20123
BUFSIZ = 128
ADDR = (HOST, PORT)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)


while True:
    print 'waiting for message ... '
    data, addr = udpServer.recvfrom(BUFSIZ)
    udpServer.sendto('[%s] %s' %(ctime(), data), addr)
    print '... received from and returned to: ', addr

udpServer.close()
