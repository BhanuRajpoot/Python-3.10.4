import socket

s = socket.socket()
print('Socket created.')
s.bind(('localhost', 9999))

s.listen(3)

print('waiting for connection')

while True:
    c, add = s.accept()
    print('Connected with...', add)

    c.send(bytes('Welcome to socket programming...', 'utf-8'))