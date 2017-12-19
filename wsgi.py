#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))

import app

application = app.app

"""
部署到 gunicorn 后
gunicorn wsgi --bind 0.0.0.0:80

"""
"""
supervisor 

➜  ~ cat /etc/supervisor/conf.d/xx.conf

[program:xx]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:80 --pid /tmp/xx.pid
directory=/root/xx
autostart=true
"""
