from utils import jinja as j, log
from route import http_response as response


def index(request):
    body = j.template("blog/index.html")
    return response(body)


def journal(request):
    body = j.template("blog/journal.html")
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def about(request):
    body = j.template("blog/about.html")
    log.d("about", "body is \n{}".format(body))
    return response(body)


def route_dict():
    r = {
        "/": index,
        "/journal": journal,
        "/about": about,
    }
    return r
