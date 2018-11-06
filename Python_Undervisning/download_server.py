import socket

port = 5000
s = socket.socket()
host = "127.0.0.1"
s.bind((host, port))
s.listen(5)

print('Server listening....') # use ,sep or  , end. sep = separator


while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)

    filname= 'beer.jpg'
    f = open(filname, 'rb') # open() is a filehandler which references to the file and read rb in binary
    l = f.read(1024)

    while l:
        conn.send(l)
        l = f.read(1024)

    f.close()
    conn.close()

