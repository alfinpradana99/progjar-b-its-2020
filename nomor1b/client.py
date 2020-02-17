import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)


try:
    # request file
    file = input("masukan nama file")
    print("sedang mengirim file ...")
    sock.sendall(file.encode())
    #untuk menerima file
    while 1:
        data = sock.recv(1024)
        file = open ("dariserver_" + file, 'wb')
        if not data:
            file.close()
            break
        file.write(data)
    print('file "%s" selesai diterima' % file)
finally:
    print ('closing socket')
    sock.close()