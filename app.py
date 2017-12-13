import socket

import os

from config import config
from request import Request
from utils import log
from route.blog import route_dict as route_blog
from route.static import route_dict as route_static

TAG = 'server'


def route_a():
    pass


def route_404(request):
    return b"HTTP/1.1 200 OK\r\n\r\n<h1>404</h1>"


def response_for_path(request):
    routes = {}
    routes.update(route_blog())
    routes.update(route_static())
    log.d(TAG, request.path)
    route = routes.get(request.path, route_404)
    return route(request)


def server_run():
    host = config['host']
    port = config['port']
    with socket.socket() as s:
        s.bind((host, port))
        log.i("host is {} , port is {}".format(host, port), write='log')

        while True:
            s.listen(5)
            conn, address = s.accept()
            log.i("conn is {} , address is {}".format(conn, address), write=True)
            r = conn.recv(1024)
            if len(r) > 0:
                request = Request.build(r)

                log.i("request is {} ".format(request))

                response = response_for_path(request)
                conn.sendall(response)
            else:
                # sometimes chrome will send empty request
                log.d("get a empty request")

            conn.close()


def init():
    print("pwd {}".format(os.getcwd()))
    os.chdir("/root/web-app/PythonWebToy")


if __name__ == '__main__':
    init()
    server_run()
