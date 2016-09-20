from socket import *

HOST = 'localhost'
PORT = 20123
BUFSIZ = 128
ADDR = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break

    udpClient.sendto(data, ADDR)

    data, ADDR = udpClient.recvfrom(BUFSIZ)
    print data
    if not data:
        break

udpClient.close()