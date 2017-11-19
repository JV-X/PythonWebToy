def index(request):
    return b"HTTP/1.1 200 OK\r\n\r\n<h1>hello python web a !</h1>"


def list(request):
    pass


def detail(request):
    pass


def route_dict():
    r = {
        "/": index,
        "/list": list,
        "/detail": detail,
    }
    return r
