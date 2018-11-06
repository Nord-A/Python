import socket
import multiprocessing
import time
import threading
import queue


# for at oprette forbindelse med bash nc 127.0.0.1 9000


clients = []
messages = queue.Queue()

host = "127.0.0.1"
port = 9000

connection = socket.socket()
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

connection.bind((host,port))

connection.listen(1)

def acceptConnection():
    names = 0
    while True:

        conn, addr = connection.accept()
        client_dict = {"NICKNAME": names, "HEARTBEAT": time.time(), "CLIENT": conn}
        clients.append(client_dict)
        names+=1
        print("New client joined the chat", addr)
        t = threading.Thread(target=client_thread, args=(conn,))
      #  p = multiprocessing.Process(target=client_thread, args=(conn,))
        t.start()

def broadcast_messages():
    while True:
        msg = messages.get()
        for c in clients:
            c["CLIENT"].send("-".encode() + msg.encode())


def client_thread(conn):
    while True:
        #print("New client thread spawned")
        msg = conn.recv(1024).decode()
        messages.put(msg)
        print("New message", msg)

       

threading.Thread(target=broadcast_messages).start()
acceptConnection()