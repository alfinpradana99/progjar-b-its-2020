import socket
import sys
import base64

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = 8888
server_address = ('localhost', portnum)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("list ")
    req = command.encode()
    print(req)
    sock.send(req)
    konten = sock.recv(1024)
    print("list file dalam folder result:")
    print(konten.decode())
finally:
    print("closing")
    sock.close()