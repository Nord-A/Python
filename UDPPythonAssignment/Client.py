import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IPaddress = '127.0.0.1'
server_address = (IPaddress, 10000)

# message = b'This is the message.  It will be repeated.'

message0 = b'com-0 ' + bytes(IPaddress, 'utf-8')
message1 = b'com-0 accept'
message2 = b'msg-0=hello, i am a new user'
message3 = b'Ok, good to know'


try:

    # Send data
    # print('sending {!r}'.format(message))
    # sent = sock.sendto(message, server_address)

    print('sending {!r}'.format(message0))
    sent = sock.sendto(message0, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

    print('sending {!r}'.format(message2))
    sent = sock.sendto(message2, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()