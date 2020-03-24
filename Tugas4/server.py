from socket import *
import socket
import threading
import logging
import time
import sys
import base64

from machine import Machine

m = Machine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        temp = (b"")
        coba = []
        while True:
            while True:
                file = self.connection.recv(1024)

                temp = temp + file
                coba.append(file)
                size = int(sys.getsizeof(file))

                if size != 1057 :
                    break
                else :
                    self.connection.sendall(b"OK")
            file = temp

            if file:
                d = file.decode()
                hasil = m.proses(d)
                print(hasil)
                self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8888))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()
