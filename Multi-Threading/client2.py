

import socket


def Main():
	host = '127.0.0.1'
	port = 5559
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	message = input('Enter the Grocery item number ->')
	while True:
		s.send(message.encode('ascii'))
		data = s.recv(1024)
		print('Recieved from the server :',str(data.decode('ascii')))
		ans = input('\nWant to buy more :')		
		if ans == 'y':
			message = input('Enter the Grocery item number-> ->')
		else:
			break
	s.close()

if __name__ == '__main__':
	Main()
