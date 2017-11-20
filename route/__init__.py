def http_response(body, headers=None):
    header = response_with_headers(headers)
    r = header + '\r\n' + body
    return r.encode()


def response_with_headers(headers=None, status_code=200):
    header = 'HTTP/1.1 {} GUA\r\nContent-Type: text/html\r\n'
    header = header.format(status_code)
    if headers is not None:
        header += ''.join([
            '{}: {}\r\n'.format(k, v) for k, v in headers.items()
        ])
    return header
