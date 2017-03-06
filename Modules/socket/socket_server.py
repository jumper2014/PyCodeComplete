import socket
s = socket.socket()
host = socket.gethostname()
port = 8088
s.bind((host, port))

s.listen(5)

while True:
    c, address = s.accept()
    print 'Got connection from ', address
    c.send('Thanks for your connection')
    c.close()