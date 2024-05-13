import socket

from util import *

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = read(conn)
    if not data:
        break
    send_bytes(conn, data.upper())

conn.close()

