import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    message = 'alfintest.txt'
    buka = open(message, 'rb')
    baca = buka.read()
    sock.sendall(baca)
    # Look for the response
finally:
    print (sys.stderr, 'closing socket')
    sock.close()