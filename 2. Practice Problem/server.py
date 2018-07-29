import socket               
 
s = socket.socket()         
print "Socket successfully created"

 
port = 12345               
 
s.bind(('', port))        
print "socket binded to %s" %(port)

s.listen(5)     
print "socket is listening"           
 
while True:
 
   c, addr = s.accept()     
   print 'Got connection from', addr

   data=c.recv(1024)
   
   a=""
   for i in range(0,len(data)):
      if(data[i]=='a' or data[i]=='e' or data[i]=='i' or data[i]=='o' or data[i]=='u' or data[i]=='A' or data[i]=='E' or data[i]=='I' or data[i]=='O'):
         a=a+'#'
      else:
         a=a+data[i]

   if not data:
     break
   
   c.sendall(a)


   c.close()
