import socket
from _thread import *
import threading
print_lock = threading.Lock()
d = {'1':('tomato',20),'2':('potato',10),'3':('onion',40),'4':('carrot',10),'5':('apple',45)}
def threaded(c):
	while True:
		print('\nList what the store has->')
		for keys in d.keys():
			name , cost = d[keys]	
			print('Keys->',keys,'Grocery -> :',name,'\n','The cost is :',cost)
		data = c.recv(1024)
		if not data:
			print('Bye')
			print_lock.release()
			break	
		name , cost = d[str(data.decode('ascii'))]
		print('Grocery selected-> :',name,'\n','Cost-> :',cost)
		ans = input('\nDo you want to checkout->')	
		if ans =='y':
			c.send(str.encode('\nYour bill is :'+str(cost)))
		else:
			print('Thank u')
	c.close()

def Main():
	host = ""
	port = 5559
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((host,port))
	s.listen(5)
	while True:
		c,addr = s.accept()
		print_lock.acquire()
		print('Connected to :',addr[0],':',addr[1])
		start_new_thread(threaded,(c,))
	s.close()


if __name__ == '__main__':
	Main()
