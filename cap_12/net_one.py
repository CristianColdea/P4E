import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#fout = open('romeo.txt', 'w')

#print()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
#    fout.write(data.decode())

#fout.close()

mysock.close()
