import socket
import sys
import base64

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = 8888
server_address = ('localhost', portnum)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("get ")
    filename = input("Masukan nama file: ")
    f = open(filename, 'wb')
    req = command.encode() + filename.encode()
    print(req)
    sock.send(req)
    konten = sock.recv(1024)
    temp = (b"")
    while True:
        temp = temp + konten
        print(konten)
        if sys.getsizeof(konten) != 1057:
            break
        else :
            konten = sock.recv(1024)
    temp = base64.b64decode(temp)
    f.write(temp)
    f.close()
    print("File telah diterima")
finally:
    print("closing")
    sock.close()
