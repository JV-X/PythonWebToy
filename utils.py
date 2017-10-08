import time


class Log(object):
    def __print(self, lever, text, **kwargs):
        print("[{}]  {}\t{}".format(lever, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , text))

    def f(self, text, **kwargs):
        self.__print("F", text, **kwargs)

    def e(self, text, **kwargs):
        self.__print("E", text, **kwargs)

    def w(self, text, **kwargs):
        self.__print("W", text, **kwargs)

    def d(self, text, **kwargs):
        self.__print("D", text, **kwargs)

    def i(self, text, **kwargs):
        self.__print("I", text, **kwargs)

    def v(self, text, **kwargs):
        self.__print("V", text, **kwargs)


log = Log()
