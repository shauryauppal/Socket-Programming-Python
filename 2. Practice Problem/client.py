import socket               
 
s = socket.socket()         
 
port = 12345               
 
s.connect(('127.0.0.1', port))



input_string = raw_input("Enter data you want to send->")
s.sendall(input_string)

print s.recv(1024)

s.close()  
