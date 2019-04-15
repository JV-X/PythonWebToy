from model.journal import Journal
from utils import jinja, log, static_txt
from route import http_response as response
import config

TAG = "routes_blog"


def index(request):
    body = jinja.template("blog/index.html", config=config.config)
    return response(body)


def journal(request):
    id = request.query['id']
    j = Journal.find_by_id(id)
    body = jinja.template("blog/journal.html", journal=j, config=config.config)
    return response(body)


def journals(request):
    a = Journal.all()
    body = jinja.template("blog/journals.html", journals=a, config=config.config)
    return response(body)


def about(request):
    body = jinja.template("blog/about.html", config=config.config)
    return response(body)


def for_melody(request):
    j = Journal()
    j.title = "张迪"
    j.content = static_txt("1.md").decode(encoding='utf-8', errors='strict')
    body = jinja.template("blog/journal.html", journal=j, config=config.config)
    return response(body)


def route_dict():
    r = {
        "/": index,
        "/journal": journal,
        "/journals": journals,
        "/melody": for_melody,
        "/about": about,
    }
    return r
