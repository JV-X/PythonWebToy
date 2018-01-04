from utils import jinja, log, check_authorized
from route import http_response as response


def auth(request):
    key = request.body
    log("doAuth, key is {}".format(key))

    if check_authorized(key):
        body = "<h1>233</h1>"
    else:
        body = jinja.template("blog/access_deny.html")

    return response(body)


def route_dict():
    r = {
        "/api/auth": auth,
    }
    return r
