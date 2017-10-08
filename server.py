import socket
from utils import log


def route_a():
    return b"HTTP/1.1 200 OK\r\n\r\n<h1>hello python web a !</h1>"


def route_b():
    return b"HTTP/1.1 200 OK\r\n\r\n<h1>hello python web  b !</h1>"


def response_for_path(path):
    """
    :param path: the target file of client
    :return: a route method
    """
    routes = {
        '/': route_a,
        '/123': route_b,
        '/favicon.ico': route_b,
    }
    route = routes.get(path)
    return route()


def server_run(host='', port=3000):
    with socket.socket() as s:  # 1st. gain a socket
        s.bind((host, port))  # 2nd. bind socket to target port
        log.i("host is {} , port is {}".format(host, port))

        while True:
            s.listen(5)  # socket start listening
            conn, address = s.accept()  # gain the client connection and  address

            request = conn.recv(1024).decode("utf-8")  # gain the request content from client
            parts = request.split()
            log.i("request is {} part is {}".format(request, parts))

            if len(parts) > 0:
                path = parts[1]
                response = response_for_path(path)
                conn.sendall(response)  # send response
            else:
                # sometimes chrome will send empty request
                log.d("get a empty request")

            conn.close()


if __name__ == '__main__':
    local_config = dict(
        host="0.0.0.0",
        port=2000,
    )
    server_run(**local_config)
