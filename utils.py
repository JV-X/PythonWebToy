import time
import platform
from jinja2 import FileSystemLoader, Environment


class Log(object):
    """ log level """
    FATAL = 'F'
    ERROR = 'E'
    WARNING = 'W'
    DEBUG = 'D'
    INFO = 'I'
    VERBOSE = 'V'

    def __admit(self, *args, **kwargs):
        kw = kwargs.copy()

        lv = kw.pop('level')
        priority = {
            'F': 5,
            'E': 4,
            'W': 3,
            'D': 2,
            'I': 1,
            'V': 0,
        }
        return priority[lv] >= priority[self.filter]

    def __args(self, lv, *args, **kw):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        a = list(args)
        tag = ""
        if 'tag' in kw:
            tag = kw.pop('tag')
        msg = "[{}]\t{}\t{}".format(lv, t, tag).ljust(40)
        a[0] = "{}\t{}".format(msg, a[0])
        return a

    def __print(self, *args, **kw):
        if not self.__admit(*args, **kw):
            return

        a = self.__args(kw.pop('level'), *args, **kw)

        if "write" in kw:
            w = kw.pop('write')
            if isinstance(w, bool):
                if w:
                    path = 'default.log'
                else:
                    print(*a, **kw)
                    return
            else:
                path = w
            with open(path, 'a', encoding='utf-8') as f:
                print(*a, file=f, **kw)

        print(*a, **kw)

    def f(self, *args, **kw):
        kw["level"] = self.FATAL
        self.__print(*args, **kw)

    def e(self, *args, **kw):
        kw["level"] = self.ERROR
        self.__print(*args, **kw)

    def w(self, *args, **kw):
        kw["level"] = self.WARNING
        self.__print(*args, **kw)

    def d(self, *args, **kw):
        kw["level"] = self.DEBUG
        self.__print(*args, **kw)

    def i(self, *args, **kw):
        kw["level"] = self.INFO
        self.__print(*args, **kw)

    def v(self, *args, **kw):
        kw["level"] = self.VERBOSE
        self.__print(*args, **kw)

    def __init__(self):
        """
        by set self.filter to different value, you can easy to control all your print
        """
        self.filter = self.VERBOSE


class Jinja(object):
    def __init__(self):
        path = 'template'
        loader = FileSystemLoader(path)
        self.env = Environment(loader=loader)

    def template(self, *args, **kwargs):
        path = args[0]
        t = self.env.get_template(path)
        return t.render(*args[1:], **kwargs)


def platform_type():
    return platform.system()


def check_authorized(key):
    path = "/root/.ssh/authorized_keys"
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline()
        while len(line) > 0:
            if key == line:
                return True
            else:
                line = f.readline()
                continue
    return False


def static_txt(name):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    path = 'static/txt/' + name
    with open(path, 'rb') as f:
        binary = f.read()
        return binary


log = Log()
jinja = Jinja()
session = []
