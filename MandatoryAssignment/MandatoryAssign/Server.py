import socket
import threading
import ScriptLanguage
import HTTPResponseMessages
import datetime
import queue

host = "127.0.0.1"
port = 9000

connection = socket.socket()
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind((host,port)) # Bind host and port to connection
connection.listen(5) # Queue set to 5


def acceptConnecetions():
    while True:
        conn, addr = connection.accept()
        print("New client joined the chat", addr)

        request_queue = queue.Queue()
        request_queue.put(conn)
        if request_queue.qsize() < 5:
            t = threading.Thread(target=client_thread, args=(conn,))
            t.start()
            request_queue.get()


def client_thread(conn):
    HTTP_request = conn.recv(1024).decode()
    logfile = open("RequestLogFile.txt", "a")

    print(HTTP_request)
    header, rest = HTTP_request.split('\r\n', 1)
    logfile.write(header + " Time: " + str(datetime.datetime.now()) +"\n")
    request_type, path, rest2 = header.split(' ')
    if request_type == "GET":
        if path == "/" or path == '/favicon.ico':
            print(path)
            with open("index.html", 'r') as f:
                html_to_ScriptLanguage_py = f.read()
                html_from_ScriptLanguage_py = ScriptLanguage.parse_html_custom(html_to_ScriptLanguage_py)
                HTTPResponseMessages.response_parser_header(html_from_ScriptLanguage_py, conn)
        else:
            try:
                with open(path[1:], 'r') as f:
                    html_to_ScriptLanguage_py = f.read()
                    html_from_ScriptLanguage_py = ScriptLanguage.parse_html_custom(html_to_ScriptLanguage_py)
                    HTTPResponseMessages.response_parser_header(html_from_ScriptLanguage_py, conn)
            except FileNotFoundError:
                with open("404.html", 'r') as f:
                    html_to_ScriptLanguage_py = f.read()
                    html_from_ScriptLanguage_py = ScriptLanguage.parse_html_custom(html_to_ScriptLanguage_py)
                    HTTPResponseMessages.response_parser_404(html_from_ScriptLanguage_py, conn)
            except:
                print("Unknown exception")


acceptConnecetions()
