import socket

from util import *

IP = "217.144.98.67"
sock = socket.socket()
sock.connect((IP, 9090))

while True:
    s = input()
    if s == "" or s == "close":
        break
    send(sock, s)
    data = read(sock)
    print(data)

sock.close()
