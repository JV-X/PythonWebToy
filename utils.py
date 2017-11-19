import time


class Log(object):
    """ log level """
    FATAL = 'F'
    ERROR = 'E'
    WARNING = 'W'
    DEBUG = 'D'
    INFO = 'I'
    VERBOSE = 'V'

    def __admit(self,  *args, **kwargs):
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
        return priority[lv] >= priority[self.filter] and len(args) > 0

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
        if not self.__admit( *args, **kw):
            return

        a = self.__args(kw.pop('level'), *args, **kw)

        if "write" in kw:
            w = kw.pop('write')
            if isinstance(w, bool):
                path = 'default.log'
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


log = Log()
