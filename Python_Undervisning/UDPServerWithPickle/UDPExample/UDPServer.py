import socket
import pickle

# Create a UDP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port

server_address = ('localhosl', 10000)

sock.bind(server_address)

while True:
    print("\nWaiting to recieve message")
    data, address = sock.recvfrom(4096)
    data_variable = pickle.loads(data)
    print(data_variable)