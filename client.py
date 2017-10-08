import socket
from utils import log


def parsed_url(url):
    """
    decode url, return protocol,host,port,path
    """
    # decode protocol
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url

    # decode path
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    if host.find(':') != -1:
        h = host.split(':')
        host = h[0]
        port = int(h[1])
    else:
        # decode port
        port_dict = {
            'http': 80,
            'https': 443,
        }
        # default port
        port = port_dict[protocol]

    return protocol, host, port, path


def response_by_socket(s):
    """
    :param s: a socket where the response from
    :return:  a bytes get from socket connection
    """
    response = b''
    buffer_size = 512
    while True:
        buffer = s.recv(buffer_size)
        if len(buffer) != 0:
            response += buffer
        else:
            return response


def get(url):
    protocol, host, port, path = parsed_url(url)

    s = socket.socket()  # 1st: gain socket ( use ssl.wrap_socket(s) for https)

    s.connect((host, port))  # 2nd. connect

    ip, port = s.getsockname()
    log.i("local ip is {} ,local port is {}".format(ip, port))

    # use Connection:close for use buffer when read from socket
    request = "GET / HTTP/1.1\r\nhost:{}\r\nConnection: close\r\n\r\n".format(host).encode("utf-8")
    s.send(request)  # 3rd. send
    log.i("request is {}".format(request))

    response = response_by_socket(s)  # 4th. receive

    log.i("response is \n{}".format(response.decode("utf-8")))


if __name__ == '__main__':
    get("www.baidu.com")
