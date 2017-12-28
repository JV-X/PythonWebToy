from model.journal import Journal
from utils import jinja, log
from route import http_response as response
import config


def index(request):
    body = jinja.template("blog/index.html", homepage=config.config['homepage'], owner=config.config["owner"])
    return response(body)


test = """
今天上课, 主要是
----------------

1. flask 中设置 cookie 和 session 的方法
2. 修复注册登录和其他用户相关功能
3. 用 pure css 美化页面
4. 用 博客 来讲解如何拆分任务


分解博客
--------

1. 准备 model
    - 博客 model， Blog
        - id
        - title
        - content
        - author
        - created_time
        - updated_time
    - 博客 model，Comment
        - id
        - username
        - content
        - created_time
        - updated_time
        - blog_id
2. 写出操作场景的文档 （你要对这些数据做什么操作，这是最重要的一步）
    - 有一个主页，可看到所有博客的标题和时间
        - 主页有链接转到发表博客的页面
        - 主页可以点博客标题进入博客详细页面
    - 发表博客页面有一个表单可以发表博客
    - 博客的详细页面，可以看到如下数据
        - 标题，作者，内容，时间
        - 所有评论的列表
        - 有一个输入框，可以输入评论
        - 输入之后，页面可以看到最新的评论
3. 根据文档，写好 CRUD 操作和其他操作
    - `Blog.all()`
    - `Blog.new()`
    - `Blog.find()`
    - `Comnet.all()`
    - `Comnet.find_by(blog_id)`
    - `Comnet.new()`
4. 写路由函数
5. 画 HTML 页面
6. 用 JS 实现相关页面的逻辑
7. 美化页面
"""

def journal(request):
    j = Journal()
    j.title = "111"
    j.content = test
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
