from utilities import *
from hashlib import sha1
import shutil

class Mover():
    def __init__(self, password='000000'):
        self.username, self.path = make_dir()
        self.password = password
        self.hash = None

    def check(self, file):
        return sha1(file.read()).hexdigest() == self.hash

    def encrypt(self):
        zip_all_files(self.path)
        with open("temp.zip", "rb") as file:
            if not self.check(file):
                file.seek(0, os.SEEK_SET)
                encrypt(file ,self.password)
                self.hash = sha1(file.read()).hexdigest()
            else:
                print("All files have already encrypted.")
                return
        # Move the encrypted file to OneDrive
        dst_path = "C:\\Users\\" + self.username + "\\OneDrive - whu.edu.cn"
        shutil.move("Encrypted_file", os.path.join(dst_path, "Encrypted_file"))


    def decrypt(self, path):
        with open(path, "rb"):
            pass

if __name__ == '__main__':
    mover = Mover()
    mover.encrypt()