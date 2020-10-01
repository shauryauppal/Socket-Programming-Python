import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',9999))
print('server is listening')
while True:
    data =s.recvfrom(1024)
    s.sendto(data[0],data[1])
s.close()
