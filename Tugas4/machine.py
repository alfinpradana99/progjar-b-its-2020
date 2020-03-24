from handle import Feature
import json
import logging

f = Feature()

class Machine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()

            if (command=='put'):
                print("Menaruh file")
                filename = cstring[1].strip()
                konten = cstring[2].strip()
                f.putfile(filename,konten.encode())
                return "File Berhasil Ditaruh"

            elif (command=='get'):
                print("Mengambil file")
                filename = cstring[1].strip()
                hasil = f.getfile(filename)
                return hasil[0]

            elif (command=='list'):
                print("List dalam folder result")
                filename = f.listfile()
                hasil = {"filename":filename}
                return json.dumps(hasil, indent=4)

            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    fm = Machine()
