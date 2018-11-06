import socket
import pickle

pickle_data = ["data", "horse"]

# Create a UDP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 10000)

data_string = pickle.dumps(pickle_data)
sent = sock.sendto(data_string, server_address)