import socket

import os

import _thread

import config
from request import Request
from utils import log, platform_type
from route.routes_blog import route_dict as route_blog
from route.api_admin import route_dict as api_blog
from route.static import route_dict as route_static


def route_404(request):
    return b"HTTP/1.1 200 OK\r\n\r\n<h1>404</h1>"


def response_for_path(request):
    log.i("request is {}".format(request))
    routes = {}
    routes.update(route_blog())
    routes.update(api_blog())
    routes.update(route_static())

    route = routes.get(request.path, route_404)
    return route(request)


def server_run():
    host = config.config['host']
    port = config.config['port']
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        log.i("host is {} , port is {}".format(host, port), write='log')
        s.listen(5)

        while True:
            conn, address = s.accept()
            log.i("conn is {} , address is {}".format(conn, address), write=True)
            _thread.start_new_thread(process_request, (conn,))


def process_request(conn):
    buffer_size = 1024
    r = b""
    buffer = conn.recv(buffer_size)
    while True:
        r += buffer
        if len(buffer) < buffer_size:
            break
        else:
            buffer = conn.recv(buffer_size)
            log.d("len(buffer) >= buffer_size")

    request = Request.build(r)
    response = response_for_path(request)
    conn.sendall(response)
    conn.close()


def init():  # 临时处理, 解决服务器上工作路径不对导致的问题
    _sys = platform_type()
    if _sys == "Linux":
        os.chdir("/root/web-app/PythonWebToy")
        config.config = config.server
    elif _sys == "Windows":
        config.config = config.local
    else:
        pass


if __name__ == '__main__':
    init()
    server_run()
