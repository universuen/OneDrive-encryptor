import os
import getpass
import zipfile

def encrypt(file, password):
    with open("Encrypted_file", "wb") as dst_file:
        count = 0  # 当前密码加密索引
        for line in file:  # 通过迭代器逐行访问
            for now_byte in line:  # 通过迭代器逐字符处理
                new_byte = now_byte ^ ord(password[count % len(password)])
                count += 1
                dst_file.write(bytes([new_byte]))


# Compress E-Onedrive directory
def zip_all_files(path):
    with zipfile.ZipFile("temp.zip", "w") as zip_file:
        zip_file.write(path, compress_type=zipfile.ZIP_DEFLATED)

def make_dir():
    username = getpass.getuser()
    path = "C:\\Users\\" + username + "\\E-OneDrive"
    if not os.path.exists(path):
        os.makedirs(path)
    return (username, path)

if __name__ == '__main__':
    make_dir()