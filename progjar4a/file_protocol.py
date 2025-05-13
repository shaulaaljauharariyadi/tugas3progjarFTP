import json
import logging
import shlex

from file_interface import FileInterface

"""
* class FileProtocol bertugas untuk memproses 
data yang masuk, dan menerjemahkannya apakah sesuai dengan
protokol/aturan yang dibuat

* data yang masuk dari client adalah dalam bentuk bytes yang 
pada akhirnya akan diproses dalam bentuk string

* class FileProtocol akan memproses data yang masuk dalam bentuk
string
"""

class FileProtocol:
    def __init__(self):
        self.file = FileInterface()

    def proses_string(self, string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        try:
            c = shlex.split(string_datamasuk)
            if not c:
                raise Exception("Empty request")
            
            c_request = c[0].strip().lower()
            logging.warning(f"memproses request: {c_request}")
            params = [x for x in c[1:]]
            
            # Cek apakah method ada di FileInterface
            if hasattr(self.file, c_request):
                method = getattr(self.file, c_request)
                cl = method(params)
                return json.dumps(cl)
            else:
                raise Exception("Command tidak dikenali")
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return json.dumps(dict(status='ERROR', data='request tidak dikenali'))

if __name__ == '__main__':
    fp = FileProtocol()
    print(fp.proses_string("LIST"))
    print(fp.proses_string("GET gambar.png"))
    print(fp.proses_string("UPLOAD halo.txt aGVsbG8gd29ybGQ="))  
    print(fp.proses_string("DELETE halo.txt"))
