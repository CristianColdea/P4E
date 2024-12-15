import socket

url = input("Please enter URL: ")
host = url.split('/')[2]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET '+ url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
    poem = b""
 
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
#        print(data.decode(), end='')
        poem = poem + data
     
#    print(poem)
    pos = poem.find(b"\r\n\r\n")
    print('Header length', pos)
    print(poem[pos:].decode())

    mysock.close()
except:
    print('URL non-existent or improperly formatted.')
    exit()
