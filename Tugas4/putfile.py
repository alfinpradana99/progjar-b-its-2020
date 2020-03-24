import socket
import base64
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = 8888
server_address = ('localhost', portnum)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("put ")
    filename = input("Masukan nama file: ")
    try:
        f = open(filename, 'rb')
    except:
        print("Tidak bisa membuka file")
    else:
        content = base64.b64encode(f.read())
        f.close()
        f = open("temp","wb")
        f.write(content)
        f.close()
        f = open("temp","rb")
        request = command.encode() + filename.encode() + (b" ") + f.read(1024)
        print(request)
        while (request):
            sock.send(request)
            request = f.read(1024)
            response = sock.recv(1024)
        f.close()
        os.remove("temp")
        print(response)
finally:
    print("closing")
    sock.close()
