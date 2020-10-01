import socket
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
c.connect(('localhost',9999))
print('client waiting for connection')
while (True):
  msg=input("enter a message:")
  c.sendto(msg.encode(),('localhost',9999))
  msg=c.recvfrom(1024)
  print("Server echoed:"+msg[0].decode())
c.close()

