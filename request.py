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
        return '______ request _______ \npath  {},\nmethod  {},\n query  {},\nbody  {}\n _____________'.format(
            self.path, self.method, self.query, self.body
        )

    @classmethod
    def build(cls, request):
        """
        build Request object by bytes
        :param request: bytes from socket
        :return: a Request object
        """
        r = request.decode()
        request = Request()

        request.raw_data = r

        header, request.body = r.split('\r\n\r\n', 1)  # only once, \r\n\r\n may exist in body

        h = header.split('\r\n')  # TODO
        for line in h:
            e = line.split(':')
            request.headers[e[0]] = e[1]

        parts = h[0].split()
        request.path = parts[1]
        # 设置 request 的 method
        request.method = parts[0]
        # request.query = {} TODO :  2017.10.3  10:23
        return request
