import socket

# Create a UDP socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


TCP_IP = '127.0.0.1'

# Nedenstående og ovenstående skal evt. ændres
# TCP_IP = socket.gethostname()

# Bind the socket to the port


server_address = (TCP_IP, 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    de = bytes.decode(data)

    if de.decode == 'com-0 ' + TCP_IP:

        sent = sock.sendto("com-0 accept".encode(), TCP_IP)
        print('received {} bytes from {}'.format(len(data), address))

    else:
        sent = sock.sendto("Not working".encode(), address)
        print('received {} bytes from {}'.format(len(data), address))

    print(data)

    # if data.decode:
    #     sent = sock.sendto("Im server" .encode(), address)
    #     print('Hello Im server.')
    #     print('sent {} bytes back to {}'.format(sent, address))
