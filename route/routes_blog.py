from model.journal import Journal
from utils import jinja, log
from route import http_response as response
import config


def index(request):
    body = jinja.template("blog/index.html", homepage=config.config['homepage'], owner=config.config["owner"])
    return response(body)


def journal(request):
    j = Journal()  # TODO
    body = jinja.template("blog/journal.html", journal=j, owner=config.config["owner"])
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def journals(request):
    a = Journal.all()
    body = jinja.template("blog/journals.html", journals=a, homepage=config.config['homepage'],
                          owner=config.config["owner"])
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def about(request):
    body = jinja.template("blog/about.html", homepage=config.config['homepage'], owner=config.config["owner"])
    log.d("about", "body is \n{}".format(body))
    return response(body)


def route_dict():
    r = {
        "/": index,
        "/journal": journal,
        "/journals": journals,
        "/about": about,
    }
    return r
