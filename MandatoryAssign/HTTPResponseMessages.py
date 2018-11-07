


def response_parser_404(html, conn):
    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(html),
        'Connection': 'close',
    }

    response_headers_raw = ''.join('{}:{}\r\n'.format(k, v) for k, v in response_headers.items())
    response_protokol = 'HTTP/1.1'
    response_status = '404'
    response_status_text = 'File Not Found'  # this can be random

    # sending all this stuff
    r = "{}{}{}\r\n".format(response_protokol, response_status, response_status_text)
    conn.send(r.encode(encoding="utf-8"))
    conn.send(response_headers_raw.encode(encoding="utf-8"))
    conn.send('\r\n'.encode(encoding="utf-8"))  # to separate headers from body
    conn.send(html.encode(encoding="utf-8"))


def response_parser_header(html, conn):
    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(html),
        'Connection': 'close',
    }

    response_headers_raw = ''.join('{}:{}\r\n'.format(k, v) for k, v in response_headers.items())
    response_protokol = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'  # this can be random

    # sending all this stuff
    r = "{}{}{}\r\n".format(response_protokol, response_status, response_status_text)
    conn.send(r.encode(encoding="utf-8"))
    conn.send(response_headers_raw.encode(encoding="utf-8"))
    conn.send('\r\n'.encode(encoding="utf-8"))  # to separate headers from body
    conn.send(html.encode(encoding="utf-8"))