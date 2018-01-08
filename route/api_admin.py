import json
import uuid

from utils import jinja, log, check_authorized, session

from route import http_response as response


def auth(request):
    key = json.loads(request.body)['key']
    log.d("doAuth, key is {}".format(key))

    if check_authorized(key):
        s = uuid.uuid4()
        session.append(s)
        body = jinja.template("blog/journal_upload.html")
        return response(body, headers={"Set-Cookie": s})
    else:
        body = jinja.template("blog/access_deny.html")
        return response(body)


def route_dict():
    r = {
        "/api/auth": auth,
    }
    return r
