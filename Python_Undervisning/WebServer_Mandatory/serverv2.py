import socket
import multiprocessing
import time
import threading
import queue
import webbrowser
import os
import WebServer_Mandatory.web
import WebServer_Mandatory.scriptLanguage





# for at oprette forbindelse med bash nc 127.0.0.1 9000


clients = []
messages = queue.Queue()

host = "127.0.0.1"
port = 9000

connection = socket.socket()



connection.bind((host, port))

# Queue is set to 5
connection.listen(5)


def send_html(path, conn):
    if path == "/" or path == "/index":
        with open('web/index.html', 'r') as html_file:
            # html_to_browser = html_file.read()
            html_to_scriptLanguage = html_file.read()
            html_to_browser = WebServer_Mandatory.scriptLanguage.parse_html_custom(html_to_scriptLanguage)
    else:

        with open(path[1:], 'r') as html_file:
            html_to_scriptLanguage = html_file.read()
            html_to_browser = WebServer_Mandatory.scriptLanguage.parse_html_custom(html_to_scriptLanguage)

    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
         'Content-Length': len(html_to_browser),
         'Connection': 'close',
    }


    response_headers_raw = ''.join('{}:{}\r\n'.format(k, v) for k, v in response_headers.items())

    response_protokol = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'


    r = "{}{}{}\r\n".format(response_protokol, response_status, response_status_text)

    conn.send(r.encode(encoding="utf-8"))
    conn.send(response_headers_raw.encode(encoding="utf-8"))
    conn.send('\r\n'.encode(encoding="utf-8"))  # to separate headers from body
    conn.send(html_to_browser.encode(encoding="utf-8"))




def acceptConnection():

    while True:
        conn, addr = connection.accept()
        clients.append(conn)
        print("the first",conn) # conn er hele socket connection
        print("the second", addr) # addr er host og port
        print("New client joined the chat", addr)
        t = threading.Thread(target=parse_request, args=(conn,))
        t.start()


def parse_request(conn):

    http_request = conn.recv(1024).decode()
    logfile = open("request_logfile.txt", 'a')
    logfile.write(http_request + "\n")
    messages.put(http_request)
    print("HTTP request: ", http_request)
    header, rest = http_request.split('\r\n', 1) #HTTP_request[0] = header, HTTP_request[1 = rest]
    print("Header: ", header)
    print("Rest: ", rest)

    HTTP_request_type, path, rest2 = header.split(' ')

    if HTTP_request_type == "GET":
        try:
            if path == "/" or path == "/index":
                send_html(path, conn)
#conn.close()
            else:
                    send_html(path, conn)
        except FileNotFoundError:
             print("File not found")

             error_file = open('errors/404.html')
             html_to_browser = error_file.read()


        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
             'Content-Length': len(html_to_browser),
             'Connection': 'close',
        }



        response_headers_raw = ''.join('{}:{}\r\n'.format(k, v) for k, v in response_headers.items())

        response_protokol = 'HTTP/1.1'
        response_status = '404'
        response_status_text = 'Not Found'



        r = "{}{}{}\r\n".format(response_protokol, response_status, response_status_text)

        conn.send(r.encode(encoding="utf-8"))
        conn.send(response_headers_raw.encode(encoding="utf-8"))
        conn.send('\r\n'.encode(encoding="utf-8"))  # to separate headers from body
        conn.send(html_to_browser.encode(encoding="utf-8"))





acceptConnection()