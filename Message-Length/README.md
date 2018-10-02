# Message Length

The default / standard way of receiving data from a socket in Python is to pull a buffer size until there is no more data to receive. 
This method has no concept for how long a message is, so the idea here is to pull the first 4 bytes of the message to obtain the message size.
The server / client will then pull N chunks where N is the `ceil(message length / buffer size)` to get the rest of the message.
The message length could also be used for other purposes such as limiting/prohibiting longer messages if the service calls for it.

The only other additional thing the server/client of message length does here is JSON encode/decoding to send more structured data to and from the sockets.
