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
        self.cookies = {}
        self.body = ''

    def __repr__(self):
        return '\n______ request _______ \n' \
               'path  {},\nmethod  {},\nquery  {},\nbody  {}\n _____________' \
            .format(self.path, self.method, self.query, self.body)

    @classmethod
    def build(cls, request):
        raw = request.decode("utf-8")
        r = Request()

        r.raw_data = raw
        log.d("xxx raw_data is \n" + r.raw_data)
        header, r.body = raw.split('\r\n\r\n', 1)
        h = header.split('\r\n')

        parts = h[0].split()
        path = parts[1]

        r.method = parts[0]
        Request.parse_path(path, r)
        Request.add_headers(h[1:], r)
        Request.add_cookies(r)

        return r

    @classmethod
    def add_headers(cls, header, request):
        lines = header
        for line in lines:
            k, v = line.split(': ', 1)
            request.headers[k] = v

    @classmethod
    def parse_path(cls, path, request):
        index = path.find('?')
        if index == -1:
            request.path = path
            request.query = {}
        else:
            path, query_string = path.split('?', 1)
            args = query_string.split('&')
            query = {}
            for arg in args:
                k, v = arg.split('=')
                query[k] = v
            request.path = path
            request.query = query

    @classmethod
    def add_cookies(cls, request):
        cookies = request.headers.get('Cookie', '')
        kvs = cookies.split('; ')
        for kv in kvs:
            if '=' in kv:
                k, v = kv.split('=')
                request.cookies[k] = v
