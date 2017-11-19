import socket

from request import Request
from utils import log
from route.blog import route_dict as route_blog


def route_a():
    pass


def route_404(request):
    return b"HTTP/1.1 200 OK\r\n\r\n<h1>404</h1>"


def response_for_path(request):
    routes = {}
    routes.update(route_blog())
    route = routes.get(request, route_404)
    return route(request)


def server_run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))
        log.i("host is {} , port is {}".format(host, port), write='log')

        while True:
            s.listen(5)
            conn, address = s.accept()
            log.i("conn is {} , address is {}".format(conn, address), write=True)
            request = Request.build(conn.recv(1024))

            log.i("request is {} ".format(request))

            if len(request.raw_data) > 0:
                response = response_for_path(request)
                conn.sendall(response)
            else:
                # sometimes chrome will send empty request
                log.d("get a empty request")

            conn.close()


if __name__ == '__main__':
    config = {
        "host": "0.0.0.0",
        "port": 2000,
    }
    server_run(**config)
