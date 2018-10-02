#!/usr/bin/env python3

import json
import struct
import socket

# type: obj -> str
def encode(data):
    return json.dumps(data)

# type: str -> obj
def decode(data):
    return json.loads(data)

def main(host, port, recv_msg_len, recv_buffer):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host,port))

    # message you send to server
    message = encode({
        "name": "test-message",
        "message": "sending message to socket client"
    })
    
    while True:
        # message sent to server
        msg = struct.pack(">I", len(message)) + message.encode("utf-8")
        s.send(msg)

        # messaga received from server
        data = None
        total_len = 0
        while total_len < self.RECV_MSG_LEN:
            msg_len = sock.recv(recv_msg_len)
            total_len = total_len + len(msg_len)
            
        # If the message has the length prefix
        if msg_len:
            data = ""
            msg_len = struct.unpack(">I", msg_len)[0]
            total_data_len = 0
            while total_data_len < msg_len:
                chunk = sock.recv(recv_buffer)
                
                if not chunk:
                    data = None
                    break
                else:
                    data = data + chunk.decode("utf-8")
                    total_data_len = total_data_len + len(chunk)
                    
        # print the received message
        # here it would be a reverse of sent message
        print("Received from the server :", decode(data).get("message", ""))

        # ask the client whether he wants to continue
        ans = input("\nDo you want to continue(y/n) :")
        if ans == "y":
            continue
        else:
            break
            
    # close the connection
    s.close()
        
if __name__ == "__main__":
    main("127.0.0.1", 10101, 4, 1024)
