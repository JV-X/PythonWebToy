import socket

host = "0.0.0.0"
port = 2000

s = socket.socket()  # 1st. as same like client ,gain a socket

s.bind((host, port))  # 2nd. bind socket to target port
print("host is {} , port is {}".format(host, port))

while True:
    s.listen(5)  # socket start listening
    conn, address = s.accept()  # gain the client connection and  address

    request = conn.recv(1024).decode("utf-8")  # gain the request content from client

    response = b"HTTP/1.1 200 OK\r\n\r\n<h1>hello python web !</h1>"

    conn.sendall(response)  # send response

    conn.close()
