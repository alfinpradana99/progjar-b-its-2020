import shelve
import uuid
import socket
import os
import base64

class Feature:
    def __init__(self):
        if not os.path.exists("result"):
            os.makedirs("result")

    # Untuk menaruh file kedalam folder result
    def putfile(self,filename=None,konten=None):
        data_file = konten
        f = open("result/"+filename,"wb")
        f.write(base64.b64decode(data_file))
        return True

    # Untuk mengambil file dari dalam folder result
    def getfile(self,filename=None):
        temp = []
        f = open("result/" + filename, "rb")
        baca = f.read()
        f.close()
        hasil = base64.b64encode(baca)
        temp.append(hasil.decode())
        return temp

    # Melakukan list untuk semua file yang ada dalam folder result
    def listfile(self):
        listfile = os.listdir("result")
        return listfile

if __name__=='__main__':
    f = Feature()