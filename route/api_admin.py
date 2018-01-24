import json
import uuid

import config
from model.journal import Journal
from utils import jinja, log, check_authorized, session

from route import http_response as response


def auth(request):
    key = json.loads(request.body)['key']
    log.d("doAuth, key is {}".format(key))

    if check_authorized(key):
        s = uuid.uuid4()
        session.append(s)
        body = jinja.template("blog/journal_upload.html", config=config.config)
        return response(body, headers={"Set-Cookie": s})
    else:
        body = jinja.template("blog/access_deny.html")
        return response(body)


def api_upload(request):
    form = json.loads(request.body)
    js = Journal.find_by(title=form["title"])

    if len(js) is 0:
        j = Journal.new(form)
        j.save()
    else:
        js[0].update(form)


def route_dict():
    r = {
        "/api/auth": auth,
        "/api/upload": api_upload,
    }
    return r
