# Guide to Socket Programming Introduction
[![HitCount](http://hits.dwyl.io/shauryauppal/Socket-Programming-Python.svg)](https://github.com/shauryauppal/Socket-Programming-Python) [![MadeIn](https://img.shields.io/badge/MADE%20IN-PYTHON-darkblue.svg)](https://github.com/shauryauppal/Socket-Programming-Python) [![MadeIn](https://img.shields.io/badge/MADE%20IN-C-yellowgreen.svg)](https://github.com/shauryauppal/Socket-Programming-Python/tree/master/Socket_C) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub stars](https://img.shields.io/github/stars/shauryauppal/Socket-Programming-Python.svg)](https://github.com/shauryauppal/Socket-Programming-Python/stargazers)

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
   + Reserves a port for computer
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

<img src = 'https://raw.githubusercontent.com/InternityFoundation/Socket-Programming-Python/master/1.%20String%20Reverse%20(Client-Server)%20Python/ReverseString.PNG' height = "430px" width = "630px"/>

 ## Reference Link
 + [Explaination and sample program geeksforgeeks](http://www.geeksforgeeks.org/socket-programming-python/)
 + [Sample Program python socket programming](http://www.bogotobogo.com/python/python_network_programming_server_client.php)

 ****************
 ## CRC Socket PROGRAMMING
 [Article Link](https://www.geeksforgeeks.org/cyclic-redundancy-check-python/)

 <img src = 'https://raw.githubusercontent.com/InternityFoundation/Socket-Programming-Python/master/3.%20Client%20Server%20CRC%20code/CRC.PNG' height = "430px" width = "630px"/>


***************
## Note - In **Socket_C** socket programming alternate C code is also added.

***************************
# SOCKET PROGRAMMING WITH MULTI-THREADING
### Checkout My Article [Socket Programming Multi-Threading At Geeksforgeeks](http://www.geeksforgeeks.org/socket-programming-multi-threading-python/)

## Socket Programming->
It helps us to connect a client to a server. Client is message sender and receiver and server is just a listener that works on data sent by client.

## What is a Thread?
A thread is a light-weight process that does not require much memory overhead, they are cheaper than processes.

## What is Multi-threading Socket Programming?
Multithreading is a process of executing multiple threads simultaneously in a single process.

## Multi-threading Modules : 
A *_thread module & threading module* is used for multi-threading in python, these modules help in synchronization and provide a lock to a thread in use.

```
from _thread import *
import threading
```
A lock object is created by->

`print_lock = threading.Lock()`

A lock has two states, "locked" or "unlocked". It has two basic methods acquire() and release(). When the state is unlocked **print_lock.acquire()** is used to change state to locked and **print_lock.release()** is used to change state to unlock.

The function **thread.start_new_thread()** is used to start a new thread and return its identifier. The first argument is the function to call and its second argument is a tuple containing the positional list of arguments.

Let's study client-server multithreading socket programming by code-\
*Note:-The code works with python3.*

# Multi-threaded Server Code


```
# import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

# thread fuction
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        data = data[::-1]

        # send back reversed string to client
        c.send(data)

    # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
```
```
Console Window:
socket binded to post 12345
socket is listening
Connected to : 127.0.0.1 : 11600
Bye
```
# Client Code
```
# Import socket module
import socket


def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host,port))

    # message you send to server
    message = "shaurya says geeksforgeeks"
    while True:

        # message sent to server
        s.send(message.encode('ascii'))

        # messaga received from server
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :',str(data.decode('ascii')))

        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()

if __name__ == '__main__':
    Main()
```

```
Console Window:
Received from the server : skeegrofskeeg syas ayruahs

Do you want to continue(y/n) :y
Received from the server : skeegrofskeeg syas ayruahs

Do you want to continue(y/n) :n

Process finished with exit code 0
```
Reference->\
<https://docs.python.org/2/library/thread.html>

*************************
## Contributions
<a href="https://github.com/shauryauppal/Socket-Programming-Python/issues"> Issues </a> and <a href ="https://github.com/shauryauppal/Socket-Programming-Python/pulls"> Pull requests </a> are most welcome.

*************

### Author:
#### Shaurya Uppal
shauryauppal00111@gmail.com

Feel free to mail me for any queries.

#### If this helped you in any way gift me a cup of coffee :coffee:
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UXSREFS2VFSWU)
