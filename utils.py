import time


class Log(object):
    """
    design like this for external easy to use,
    you can just use like log.d log.w to print any lever you want ,
    by way of set self.filter to different value, you can easy to control all your print
    """

    def __print(self, lever, text, **kwargs):
        if lever >= self.filter:
            print("[{}]  {}\t{}".format(lever, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), text), kwargs)

    def f(self, text, **kwargs):
        self.__print(self.FATAL, text, **kwargs)

    def e(self, text, **kwargs):
        self.__print(self.ERROR, text, **kwargs)

    def w(self, text, **kwargs):
        self.__print(self.WARNING, text, **kwargs)

    def d(self, text, **kwargs):
        self.__print(self.DEBUG, text, **kwargs)

    def i(self, text, **kwargs):
        self.__print(self.INFO, text, **kwargs)

    def v(self, text, **kwargs):
        self.__print(self.VERBOSE, text, **kwargs)

    def __init__(self):
        self.FATAL = 5
        self.ERROR = 4
        self.WARNING = 3
        self.DEBUG = 2
        self.INFO = 1
        self.VERBOSE = 0
        self.filter = self.VERBOSE


log = Log()
