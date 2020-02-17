import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    print(sys.stderr, 'connection from', client_address)
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(64)
        buka = open('new' + '.txt', 'a+b')
        
        print (sys.stderr, 'received "%s"' % data)

        if not data:
            buka.close()
            break
        buka.write(data)
    # Clean up the connection
    connection.close()