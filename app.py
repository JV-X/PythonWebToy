import socket

import os

import config
from request import Request
from utils import log, platform_type
from route.routes_blog import route_dict as route_blog
from route.api_auth import route_dict as api_blog
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

        while True:
            s.listen(5)
            conn, address = s.accept()
            log.i("conn is {} , address is {}".format(conn, address), write=True)
            r = conn.recv(1024)
            if len(r) > 0:
                request = Request.build(r)
                response = response_for_path(request)
                conn.sendall(response)
            else:
                # sometimes chrome will send empty request
                log.d("get a empty request")

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
