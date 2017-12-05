import sys

import os

from utils import jinja, log
from route import http_response as response
from config import config


def index(request):
    file = "blog{}index.html".format(os.sep)
    body = jinja.template(file, homepage=config['homepage'], owner=config["owner"])
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
    file = "blog{}journal.html".format(os.sep)
    body = jinja.template(file, journal=j)
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def journals(request):
    a = Journal.all()
    file = "blog{}journals.html".format(os.sep)
    body = jinja.template(file, journals=a, homepage=config['homepage'], owner=config["owner"])
    log.d("journal", "body is \n{}".format(body))
    return response(body)


def about(request):
    file = "blog{}about.html".format(os.sep)
    body = jinja.template(file, homepage=config['homepage'], owner=config["owner"])
    log.d("about", "body is \n{}".format(body))
    return response(body)


def praetorian(request):
    body = ""
    if True:
        file = "blog{}access_deny.html".format(os.sep)
        body = jinja.template(file)
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
