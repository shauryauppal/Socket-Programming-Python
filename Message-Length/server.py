#!/usr/bin/env python3

import json
import socket
import select
import struct
import threading

# type: obj -> str
def encode(data):
    return json.dumps(data)

# type: str -> obj
def decode(data):
    return json.loads(data)

_HOST = "127.0.0.1"
_PORT = 10101

class SocketServer(threading.Thread):
    MAX_WAITING_CONNECTIONS = 5
    RECV_BUFFER = 4096
    RECV_MSG_LEN = 4
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.connections = []
        self.running = True
        
    def _bind_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.MAX_WAITING_CONNECTIONS)
        self.connections.append(self.server_socket)
        
    @classmethod
    def _send(cls, sock, msg):
        # Append message with length of message
        msg = struct.pack(">I", len(msg)) + msg.encode("utf-8")
        sock.send(msg)
        
    def _receive(self, sock):
        data = None
        total_len = 0
        while total_len < self.RECV_MSG_LEN:
            msg_len = sock.recv(self.RECV_MSG_LEN)
            total_len = total_len + len(msg_len)
            
        # If the message has the length prefix
        if msg_len:
            data = ""
            msg_len = struct.unpack(">I", msg_len)[0]
            total_data_len = 0
            while total_data_len < msg_len:
                chunk = sock.recv(self.RECV_BUFFER)
                
                if not chunk:
                    data = None
                    break
                else:
                    data = data + chunk.decode("utf-8")
                    total_data_len = total_data_len + len(chunk)
        
        return data
    
    def _broadcast(self, client_socket, client_message):
        print("Starting broadcast...")
        for sock in self.connections:
            not_server = (sock != self.server_socket)
            not_sending_client = (sock != client_socket)
            if not_server and not_sending_client:
                try:
                    print("Broadcasting: %s" % client_message)
                    self._send(sock, client_message)
                except socket.error:
                    # Client no longer replying
                    print("Closing a socket...")
                    sock.close()
                    self.connections.remove(sock)
    
    def _run(self):
        print("Starting socket server (%s, %s)..." % (self.host, self.port))
        while self.running:
            try:
                # Timeout every 60 seconds
                selection = select.select(self.connections, [], [], 5)
                read_sock = selection[0]
            except select.error:
                print("Error!!!")
            else:
                for sock in read_sock:
                    # New connection
                    if sock == self.server_socket:
                        try:
                            accept_sock = self.server_socket.accept()
                            client_socket, client_address = accept_sock
                        except socket.error:
                            print("Other error!")
                            break
                        else:
                            self.connections.append(client_socket)
                            print("Client (%s, %s) is online" % client_address)
                            
                            self._broadcast(client_socket, encode({
                                "name": "connected",
                                "data": client_address
                            }))
                    # Existing client connection
                    else:
                        try:
                            data = self._receive(sock)
                            if data:
                                print(decode(data))
                                self._send(sock, data)
                        except socket.error:
                            # Client is no longer replying
                            self._broadcast(sock, encode({
                                "name": "disconnected",
                                "data": client_address
                            }))
                            print("Client (%s, %s) is offline" % client_address)
                            sock.close()
                            self.connections.remove(sock)
                            continue
        # Clear the socket connection
        self.stop()
    
    def run(self):
        self._bind_socket()
        self._run()
        
    def stop(self):
        self.running = False
        self.server_socket.close()
        
if __name__ == "__main__":
    socket_server = SocketServer(_HOST, _PORT)
    socket_server.start()
