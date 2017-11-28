from utils import log


def route_static(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', )
    log.d("filename is {}".format(filename))
    path = 'static/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\n\r\n'
        binary = header + f.read()
        return binary


def route_static_js(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', )
    log.d("filename is {}".format(filename))
    path = 'static/js/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\n\r\n'
        binary = header + f.read()
        return binary


def route_static_css(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', )
    log.d("filename is {}".format(filename))
    path = 'static/css/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\n\r\n'
        binary = header + f.read()
        return binary


def route_static_img(request):
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.query.get('file', )
    log.d("filename is {}".format(filename))
    path = 'static/img/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\n\r\n'
        binary = header + f.read()
        return binary


def route_dict():
    r = {
        '/static': route_static,
        '/static/js': route_static_js,
        '/static/css': route_static_css,
        '/static/img': route_static_img,
    }
    return r
