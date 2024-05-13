def to_bytes(s):
    return bytes(s, encoding = 'UTF-8')

def read(sock):
    size = int.from_bytes(sock.recv(4), byteorder = 'big')
    data = sock.recv(size)
    return data

def send(sock, s):
    data = to_bytes(s)
    sock.send(len(data).to_bytes(4, byteorder = 'big'))
    sock.send(data)

def send_bytes(sock, data):
    sock.send(len(data).to_bytes(4, byteorder = 'big'))
    sock.send(data)


