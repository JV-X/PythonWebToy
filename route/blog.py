from utils import jinja, log
from route import http_response as response
from config import config


def index(request):
    body = jinja.template("blog/index.html", homepage=config['homepage'], owner=config["owner"])
    return response(body)


class Journal(object):
    def __init__(self, date='',
                 display_date='', year='',
                 name='', display_name='', content=''):
        self.date = date
        self.display_date = display_date
        self.year = year
        self.name = name
        self.display_name = display_name
        self.content = content

    @staticmethod
    def all():
        js = (
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
            Journal(date='2',
                    display_date='4', year='6',
                    name='8', display_name='0'),
            Journal(date='1',
                    display_date='3', year='5',
                    name='7', display_name='9'),
        )
        return js


def journal(request):
    j = Journal()
    body = jinja.template("blog/journal.html", journal=j)
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def journals(request):
    a = Journal.all()
    body = jinja.template("blog/journals.html", journals=a, homepage=config['homepage'], owner=config["owner"])
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def about(request):
    body = jinja.template("blog/about.html", homepage=config['homepage'], owner=config["owner"])
    log.d("about", "body is \n{}".format(body))
    return response(body)


def praetorian(request):
    body = ""
    if True:
        body = jinja.template("blog/access_deny.html")
    log.d("about", "body is \n{}".format(body))
    return response(body)


def route_dict():
    r = {
        "/": index,
        "/journal": journal,
        "/journals": journals,
        "/about": about,
        "/praetorian": praetorian,
    }
    return r
