#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

# for Apache
sys.path.insert(0, abspath(dirname(__file__)))

import app

# 必须有一个叫做 application 的变量
# gunicorn 就要这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
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
