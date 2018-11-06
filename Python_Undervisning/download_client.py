import socket



s = socket.socket()
host = "127.0.0.1"
port = 5000

s.connect((host,port))
s.send("Hello server!".encode())

with open('new_mull.png', 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

f.close()
s.close()