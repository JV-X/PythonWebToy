from utils import log


class Request(object):
    def __init__(self):
        """
        use build method to gain Request Object
        """
        self.raw_data = ''
        self.method = 'GET'
        self.headers = {}
        self.path = ''
        self.query = {}
        self.body = ''

    def __repr__(self):
        return '\n______ request _______ \n' \
               'path  {},\nmethod  {},\nquery  {},\nbody  {}\n _____________' \
            .format(self.path, self.method, self.query, self.body)

    @classmethod
    def build(cls, request):
        """
        build Request object by bytes
        :param request: bytes from socket
        :return: a Request object
        """
        r = request.decode("utf-8")
        request = Request()

        request.raw_data = r
        header, request.body = r.split('\r\n\r\n', 1)  # only once, \r\n\r\n may exist in body
        h = header.split('\r\n')
        first_line = h.pop(0)
        log.d(first_line)
        for line in h:
            log.d("line is {}".format(line))
            e = line.split(':')
            request.headers[e[0]] = e[1]

        parts = h[0].split()
        request.path = parts[1]
        request.method = parts[0]
        # request.query = {} TODO :  2017.10.3  10:23
        return request
