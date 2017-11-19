import time


class Log(object):
    """
    design like this for external easy to use,
    you can just use like log.d log.w to print any lever you want ,
    by way of set self.filter to different value, you can easy to control all your print
    """

    def __print(self, lever, text, write=False, **kwargs):

        if lever >= self.filter:

            msg = "[{}]  {}\t{}".format(self.namespace[lever],
                                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                        text)

            if write:
                with open('log.test.txt', 'a', encoding='utf-8') as f:
                    print(msg, file=f, **kwargs)

            print(msg, **kwargs)

    def f(self, text, write=False, **kwargs):
        self.__print(self.FATAL, text, write, **kwargs)

    def e(self, text, write=False, **kwargs):
        self.__print(self.ERROR, text, write, **kwargs)

    def w(self, text, write=False, **kwargs):
        self.__print(self.WARNING, text, write, **kwargs)

    def d(self, text, write=False, **kwargs):
        self.__print(self.DEBUG, text, write, **kwargs)

    def i(self, text, write=False, **kwargs):
        self.__print(self.INFO, text, write, **kwargs)

    def v(self, text, write=False, **kwargs):
        self.__print(self.VERBOSE, text, write, **kwargs)

    def __init__(self):
        self.FATAL = 5
        self.ERROR = 4
        self.WARNING = 3
        self.DEBUG = 2
        self.INFO = 1
        self.VERBOSE = 0
        self.namespace = {
            5: "F",
            4: "E",
            3: "W",
            2: "D",
            1: "I",
            0: "V",
        }

        self.filter = self.VERBOSE


log = Log()
