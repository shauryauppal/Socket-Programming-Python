# Guide to Socket Programming Introduction

## Socket programming is started by socket library

```
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```

+ AF_INET refers to address family ipv4
+ SOCK_STREAM meaning TCP protocol

*****************


## SERVER code
+ s = socket.socket()
   + It simply creates a new socket using the given address family,socket type and protocol number.
+ port = 12345
   + Reverse a port for computer
+ s.bind('',port)
  + We binded our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well. If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
+ s.listen(5)
   + Server can connect to 5 clients, 6th or more clients are rejected.
+ s.accept()
   + Return new socket object c and address
+ s.close()
  + Marks the socket closed, all future operaions on socket will be failed.
 
 #### OverView
  ```
 #import library
 import socket
 
 s=socket.socket()
 port=12345
 s.bind('',port)
 s.listen(5)
 
 while True:
   c,addr = s.accept()
   data = c.recv(1024)
   c.sendall(data)
 c.close()
```
Server uses `bind() , listen() , accept()`
*************
## Client Code

+ First create socket object
+ Give port number same as server
+ connect() '127.0.0.1' local machine connection
+ print s.recv(1024) #print data recv from socket
+ close() connection
```
 import socket
 s=socketsocket()
 port=12345
 s.connect('127.0.0.1',port)
 print s.recv(1024)
 s.close()
```
 
 ## Reference Link
 + [Explaination and sample program geeksforgeeks](http://www.geeksforgeeks.org/socket-programming-python/)
 + [Sample Program python socket programming](http://www.bogotobogo.com/python/python_network_programming_server_client.php)
 
***************
## Note - In **Socket_C** socket programming alternate C code is also added.
