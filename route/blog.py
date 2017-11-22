from utils import jinja as j, log
from route import http_response as response


def index(request):
    body = j.template("blog/index.html", homepage='127.0.0.1:2000',owner="XJV")
    return response(body)


class Journal(object):
    def __init__(self, date='',
                 display_date='', year='',
                 name='', display_name=''):
        self.date = date
        self.display_date = display_date
        self.year = year
        self.name = name
        self.display_name = display_name

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
        )
        return js


def journal(request):
    a = Journal.all()
    body = j.template("blog/journal.html", journals=a, homepage='127.0.0.1:2000',owner="XJV")
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def about(request):
    body = j.template("blog/about.html", homepage='127.0.0.1:2000',owner="XJV")
    log.d("about", "body is \n{}".format(body))
    return response(body)


def route_dict():
    r = {
        "/": index,
        "/journal": journal,
        "/about": about,
    }
    return r
