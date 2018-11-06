import socket
import threading
import queue
import WebServer_Mandatory.scriptLanguage
import WebServer_Mandatory.errors
import WebServer_Mandatory.web
from WebServer_Mandatory import scriptLanguage

# clients = []
# messages = queue.Queue()#Thread safe


host = "127.0.0.1"
port = 9000

connection = socket.socket()
connection.bind((host, port))
connection.listen(5)


def find_html_file(path):
    try:
        if path == "/":
            with open('web/index.html', 'r') as f:
                html_file = f.read()
                html_parsed = scriptLanguage.parse_html_custom(html_file)
        else:
            with open(path[1:], 'r') as f:
                html_file = f.read()
                html_parsed = scriptLanguage.parse_html_custom(html_file)
        response_status = "200"
        response_status_text = "OK"
        return html_parsed, response_status, response_status_text
    except FileNotFoundError:
        with open("errors/404.html", 'r') as f:
            html_file = f.read()
            response_status = "404"
            response_status_text = 'Not Found'
            return html_file, response_status, response_status_text


def send_html(path, conn):
    tree, response_status, response_status_text = find_html_file(path)

    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(tree),  # msg
        # 'Connection': 'close',
    }

    response_headers_raw = ''.join('{}: {}\r\n'.format(k, v) for k, v in response_headers.items())

    response_proto = 'HTTP/1.1'

    # sending all this stuff
    r = '{}{}{}\r\n'.format(response_proto, response_status, response_status_text)
    conn.send(r.encode(encoding="utf-8"))
    conn.send(response_headers_raw.encode(encoding="utf-8"))
    conn.send('\r\n'.encode(encoding="utf-8"))  # to separate headers from body
    conn.send(tree.encode(encoding="utf-8"))  # msg.


def accept_connections():
    while True:
        conn, addr = connection.accept()
        # clients.append(conn)
        print("New client joined the chat", addr)
        t1 = threading.Thread(target=parse_request, args=(conn,))  #tuple because of ,. not a tuple if one value
        t1.start()


def parse_request(conn):

    http_request = conn.recv(1024).decode()

    #Log http request
    logfile = open("request_logfile.txt", "a")
    logfile.write(http_request + "\n")

    # print("\n\n -----")
    # print(http_request)
    # print("\n\n -----")

    header, rest = http_request.split('\r\n', 1)  # http_request[0] = header, http_request[1] = rest
    print("header:", header)
    print("rest:", rest)

    request_type, path, rest2 = header.split(' ')
    if request_type == "GET":
        try:
            send_html(path, conn)
        except:
            print("General error!")


accept_connections()