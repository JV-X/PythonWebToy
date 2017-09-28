import socket

s = socket.socket()  # 1st: gain socket ( use ssl.wrap_socket(s) for https)

host = "baidu.com"
port = 80

s.connect((host, port))  # 2nd. connect

ip, port = s.getsockname()
print("local ip is {} ,local port is {}".format(ip, port))

request = "GET / HTTP/1.1\r\nhost:{}\r\n\r\n".format(host).encode("utf-8")
s.send(request)  # 3rd. send
print("request is {}".format(request))

response = s.recv(1024)  # 4th. receive

print("buffer is {}".format(response.decode("utf-8")))

