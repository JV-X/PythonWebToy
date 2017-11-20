from utils import jinja as j, log
from route import http_response as response


def index(request):
    body = j.template("blog_index.html")
    return response(body)


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
